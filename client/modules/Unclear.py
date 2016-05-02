# -*- coding: utf-8-*-
from sys import maxint
import random

WORDS = []

PRIORITY = -(maxint + 1)


def handle(text, mic, profile):
    """
        Reports that the user has unclear or unusable input.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    messages = ["hi 能重复一次吗",
                "抱歉，能再说一遍吗？",
                "oh 请重复一遍", "不好意思，没听清楚。"]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    return True
