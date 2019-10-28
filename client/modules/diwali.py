import random
import re


WORDS = ["HAPPY","DIWALI"]

def isValid(text):
    """
        Returns True if the input is related to happy diwali wishes.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bhappy diwali\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        diwali wishes.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["Happy diwali to you to",
    "shubh deepawali Aahana",
    "Happy diwali. May this diwali bring prosparity to you and your family"

    ]   
    message = random.choice(messages)

    mic.say(message)
