# -*- coding: utf-8-*-
import datetime
import re
import os

# WORDS = ["TIME"]
WORDS = ["服务器","开启","关闭"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    if u'关' in text:
        echo = os.system('ssh root@192.168.5.200 "shutdown -h now"')
        if echo == "":
            mic.say("服务器已经关闭")
        else:
            mic.say(u"关闭指令出现问题，执行未成功。" + str(echo) )
    elif u'开' in text:
        os.system('wakeonlan 90:2b:34:2b:ff:6a')
        mic.say("已经向服务器发出启动指令，稍后即可登录。")        
    elif u"重启" in text:
        os.system('ssh root@192.168.5.200 "reboot"')
        mic.say("重启指令已经执行，服务器重启中，稍后即可登录。")
    


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'服务器', text, re.IGNORECASE))
