import argparse
import smtplib
import yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from participant import Participant, build_participant_list_from_config, simulate_drawing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate picking names out of a hat for a secret santa gift exchange')
    parser.add_argument('--config_path', type=str, default='config.yaml', help="path to yaml config file")
    args = parser.parse_args()

    # Load config yaml file
    with open(args.config_path, "r") as f:
        config = yaml.safe_load(f)

    # Create a list of participants
    participants = build_participant_list_from_config(config)

    # Run the random simulation to pick a recipient for each person
    simulate_drawing(participants)

    # Connect to SMTP server
    smtp_server = None
    if "smtp" in config and not config.get("dry_run", False):
        smtp_server = smtplib.SMTP(config["smtp"]["host"], config["smtp"]["port"])
        if config["smtp"].get("tls", False):
            smtp_server.starttls()
        if "username" in config["smtp"] and "password" in config["smtp"]:
            smtp_server.login(config["smtp"]["username"], config["smtp"]["password"])

        # Build email
        message = MIMEMultipart("alternative")
        message["Subject"] = config["email"]["subject"]
        message["From"] = config["email"]["from"]

    # Send email to each participant
    for participant in participants:
        text = config["email"]["message"].format(name=participant.name, recipient=participant._recipient.name)
        if smtp_server:
            message["To"] = participant.email
            message.attach(MIMEText(text, "html"))
            smtp_server.sendmail(config["email"]["from"], participant.email, message.as_string())
        else:
            print(text)

    if smtp_server:
        smtp_server.close()
