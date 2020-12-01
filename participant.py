import random
from typing import List

class Participant:
    """Participant represents a person participating in the secret santa gift exchange. 
    
    Positional Arguments:
      name: Name of the participant
      email: Email address to send message to
    """
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._excludes = [self]
        self._recipient = None


def build_participant_list_from_config(config: dict) -> List[Participant]:
    """Build the list of participants from the config file

    Positional Arguments:
        config: the config dict containing settings

    Returns:
        The constructed list of participants
    """
    participants = {}
    # First create participants
    for p in config["participants"]:
        participants[p["name"]] = Participant(p["name"], p["email"])

    # Next setup exclusion rules
    for p in config["participants"]:
        participant = participants[p["name"]]
        for exclude in p.get("excludes", []):
            participant._excludes.append(participants[exclude])
    
    return list(participants.values())

def simulate_drawing(participants: List[Participant]) -> None:
    """Randomly choose a recipient for each participant

    Positional Arguments:
        participants: list of participants
    """
    try:
        pool = participants.copy()
        # Loop through each participant and choose a random person from the remaining pool of people
        for participant in participants:
            recipient = random.choice([p for p in pool if p not in participant._excludes])
            participant._recipient = recipient
            pool.remove(recipient)
    except:
        # Occasionally there will be an IndexError exception when the last person can only pick themself. Try again
        return random_picker(participants)