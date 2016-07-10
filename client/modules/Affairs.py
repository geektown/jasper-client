# -*- coding: utf-8-*-
import datetime
import re
import os

# WORDS = ["TIME"]
WORDS = [u"提醒"]

# 事务管理的指令
cmd = {"topic":"","time":"","date":"","location":""}

def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    getCmd(text)
    
def getCmd(msg):
    """
        returns resolved cmds, 通常一个事务管理必备的cmd如下，
        {
            "topic":"参加家长会",
            "time":"9点",
            "date":"7-13号",
            "location":"学校"
        }
        Arguments:
        msg -- user-input, typically transcribed speech
    """
    global cmd
    parsed = nlp_recognition(msg)
    if cmd['topic'] == "":
       cmd['topic'] = getTopic(parsed)
    for (k, v) in cmd.items():
        print k, v
       
       
def getTopic(parsed):
    topic = ""
    r_index = 0 # 人称代词的索引地址，通常是我
    for kv in parsed:
        if kv['tag'] == "r":
            break
        r_index = r_index + 1
    while parsed[r_index]:
        topic = topic + parsed[r_index]["word"]
        r_index = r_index + 1
        if r_index >= len(parsed):
            break
    return topic
            

def nlp_recognition(msg):
    return [{"word":"下","tag":"f"},{"word":"周二","tag":"t"},{"word":"下午","tag":"t"},{"word":"3","tag":"m"},{"word":"点","tag":"q"},{"word":"提醒","tag":"v"},{"word":"我","tag":"r"},{"word":"参加","tag":"v"},{"word":"家长会","tag":"n"},{"word":"。","tag":"w"}]

    
def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'提醒', text, re.IGNORECASE))
