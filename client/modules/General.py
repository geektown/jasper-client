# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

# baidu apistore
import sys, urllib, urllib2, json

WORDS = ["GENERAL", "状态测试"]



def getResponse():
    response = random.choice([u"请告诉我唐诗的名称", u"请告诉我城市名称", u"再听一遍吗？", u"对话结束"])
    return response
    
def handle(text, mic, profile):
    response = getResponse()
    print response
    # 如果返回的json中包含，play字段，则先play或者say，然后再判断是否有继续对话的提示，或者
    # {'play':'ssss.wav | this is a text', 'continue':'继续提问的内容', 'endup':'true'}
    mic.say(response.encode('utf-8'))
    if response == u"对话结束":
        return
    else:
        print "try to activeListen"
        listen = mic.generalListen() # 注意threadhold设置
        print 'try to listen in handle and got ' + "#".join(listen)
        if listen != None :
            handle(text, mic, profile)
    


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
    return bool(re.search(u'状态', text, re.IGNORECASE))
