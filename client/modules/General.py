# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

# baidu apistore
import sys, urllib, urllib2, json

WORDS = ["GENERAL", "状态测试"]

def mockRobotResponse(filename=jasperpath.data('text', 'jasper-conversation.json')):
    jsonFile = open(filename, "r")
    conversation = list()
    for text in jsonFile.readlines():
        conversation.append(text)
    return conversation
    
def getResponse(userInput):
    print userInput.encode("utf-8")
    return random.choice(mockRobotResponse())

def handle0(text, mic, profile):
    robotSay = json.loads(getResponse(text))
    next = robotSay["next"]
    if next != "finish":
        print('say or play ' + robotSay["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
        if next == "activeListen":
            print "try to activeListen"
            listen = mic.generalListen() # 注意threadhold设置
            print 'try to listen in handle and got ' + "#".join(listen)
            if listen != None :
                handle(text, mic, profile)
            else:
                mic.say("there is no answer. conversation over.")
        else:
            print "say " + next.encode('utf-8')
        robotSay = json.loads(getResponse(text))
        next = robotSay["next"]
    print(robotSay["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
    
def handle(text, mic, profile):
    robotSay = json.loads(getResponse(text))
    next = robotSay["next"]
    
    if next == "finish" :
        print(robotSay["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
        if bool(re.search(u'.mp3', robotSay["say"], re.IGNORECASE)):
            mic.playMP3('/home/pi/tangshi/05-5.mp3') 
        else:
            mic.say(robotSay["say"].encode('utf-8'))
        return

    print('say or play ' + robotSay["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
    if bool(re.search(u'.mp3', robotSay["say"], re.IGNORECASE)):
        mic.playMP3('/home/pi/tangshi/05-5.mp3') 
    else:
        print "say " + robotSay["say"].encode('utf-8')
        mic.say(robotSay["say"].encode('utf-8'))
        
    if next == "activeListen":
        print "try to activeListen"
        listen = mic.generalListen() # 注意threadhold设置
        print 'try to listen in handle and got ' + "#".join(listen)
        if listen != None :
            handle(text, mic, profile)
        else:
            mic.say("there is no answer. conversation over.")
    else:
        mic.say(next.encode("utf-8"))
        listen = mic.generalListen() # 注意threadhold设置
        print 'try to listen in handle and got ' + "#".join(listen)
        if listen != None :
            handle(text, mic, profile)
        else:
            mic.say("there is no answer. conversation over.")
        


def handle3(text, mic, profile):
    response = getResponse(text)
    print response
    # 如果返回的json中包含，play字段，则先play或者say，然后再判断是否有继续对话的提示，或者
    # {'play':'ssss.wav | this is a text', 'continue':'继续提问的内容', 'endup':'true'}
    mic.say(response.encode('utf-8'))
    if response == u"对话结束":
        return
    else:
        mic.playMP3('/home/pi/tangshi/05-5.mp3')
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
