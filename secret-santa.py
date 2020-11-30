import argparse
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from participant import Participant, random_picker

email_subject_default = "Secret Santa"
email_message_template_default = "<html><body>Hello {name},<br><br>You got {recipient} for the Secret Santa gift exchange.<br><br>Merry Christmas!</body></html>"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate picking names out of a hat for a secret santa gift exchange')
    parser.add_argument('--csv', type=str, required=True, help="path to a csv that contains all the participants' information")
    parser.add_argument('--dry_run', action='store_true', help="perform a dry test run and print the alerts to the console")
    parser.add_argument('--email_sender', type=str, required=True, help="email address to send from")
    parser.add_argument('--email_subject', type=str, default=email_subject_default, help="email subject")
    parser.add_argument('--email_message_template', type=str, default=email_message_template_default, help="alternative message template to use instead of the default")
    parser.add_argument('--smtp_host', type=str, required=True, help="host of the smtp server")
    parser.add_argument('--smtp_port', type=int, required=True, help="port of the smtp server")
    parser.add_argument('--smtp_tls', action='store_true', help="use tls when talking to smtp server")
    parser.add_argument('--smtp_username', type=str, help="user to authenticate to the smtp server")
    parser.add_argument('--smtp_password', type=str, help="password to authenticate to the smtp server")
    args = parser.parse_args()

    # Read participant information from a csv file
    participants = []
    if args.csv:
        with open(args.csv, 'r') as f:
            for row in csv.reader(f):
                participants.append(Participant(row[0], row[1]))

    # Run the random picker
    random_picker(participants)

    # Connect to SMTP server
    with smtplib.SMTP(args.smtp_host, args.smtp_port) as smtp_server:
        if args.smtp_tls:
            smtp_server.starttls()
        if args.smtp_username and args.smtp_password:
            smtp_server.login(args.smtp_username, args.smtp_password)

        # Build email
        message = MIMEMultipart("alternative")
        message["Subject"] = args.email_subject
        message["From"] = args.email_sender
    
        # Send email to each participant
        for participant in participants:
            text = participant.format_text(args.email_message_template)
            if args.dry_run:
                print(text)
            else:
                message["To"] = participant.email
                message.attach(MIMEText(text, "html"))
                smtp_server.sendmail(args.email_sender, participant.email, message.as_string())
