# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

# baidu apistore
import sys, urllib, urllib2, json

WORDS = ["JOKE", "笑话"]


def getRandomJoke(filename=jasperpath.data('text', 'JOKES.txt')):
    jokeFile = open(filename, "r")
    jokes = []
    start = ""
    end = ""
    for line in jokeFile.readlines():
        line = line.replace("\n", "")

        if start == "":
            start = line
            continue

        if end == "":
            end = line
            continue

        jokes.append((start, end))
        start = ""
        end = ""

    jokes.append((start, end))
    joke = random.choice(jokes)
    return joke

def getJokes():
    url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'
    req = urllib2.Request(url)
    req.add_header("apikey", "9306b0063beeaabe3d26f6561e34e546")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        print(content)
    data = json.loads(content)
    print(random.choice(data["showapi_res_body"]["contentlist"])['text']) ## 随机挑选一个笑话
    speechText = (random.choice(data["showapi_res_body"]["contentlist"])['text']).encode('utf-8')
    print speechText
    return speechText
    
def handle(text, mic, profile):
    mic.say(getJokes())


def handle2(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    joke = getRandomJoke()

    mic.say("Knock knock")

    def firstLine(text):
        mic.say(joke[0])

        def punchLine(text):
            mic.say(joke[1])

        punchLine(mic.activeListen())

    firstLine(mic.activeListen())


def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'笑话', text, re.IGNORECASE))
