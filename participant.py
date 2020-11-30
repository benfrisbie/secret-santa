import random
from typing import List

class Participant:
    """Participant represents an individual participating in the secret santa gift exchange. 
    
    Positional Arguments:
      name: Name of the participant
      email: Email address to send message to
    """
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._recipient = None

    def format_text(self, email_message_template: str) -> str:
        """Formats the text to send to the participant.

        Positional Arguments:
            email_message_template: message template to format

        Returns:
            The formatted text.
        """
        return email_message_template.format(name=self.name, recipient=self._recipient.name)


def random_picker(participants: List[Participant]) -> None:
    """Randomly choose a recipient for each participant

    Positional Arguments:
        participants: list of participants
    """
    try:
        pool = participants.copy()
        # Loop through each participant and choose a random person from the remaining pool of people
        for participant in participants:
            recipient = random.choice([p for p in pool if p != participant])
            participant._recipient = recipient
            pool.remove(recipient)
    except:
        # Occasionally there will be an IndexError exception when the last person can only pick themself. Try again
        return random_picker(participants)