# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import time
import urllib
import urllib2
import json

# baidu apistore
import sys, urllib, urllib2, json
PRIORITY = 999
WORDS = ["GENERAL", "状态测试"]

def request(msg):
    return [{"cmd":"say", "value":"唐诗已经找到，即将播放。"}, {"cmd":"sleep", "value":"3"}, {"cmd":"play", "value":"/home/pi/tangshi/05-5.mp3"}, {"cmd":"say", "value":"需要再听一遍吗？"}, {"cmd":"exit"}]

def post_xiaoi_openapi(text):
    url='http://115.29.199.8/openapi'
    values ={'userid':u'Smith','userinput':text}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    rdata = response.read()  # 获取服务器返回的页面信息
    print rdata    
    return rdata

def handle(text, mic, profile):
    response = json.loads(post_xiaoi_openapi(text))
    for instruction in response:
        if instruction['cmd'] == "say":
            print "say", instruction['value']
            mic.say(instruction['value'])
        elif instruction['cmd'] == "play":
            print "paly media", instruction['value']
            mic.playMP3(instruction['value']) 
        elif instruction['cmd'] == "exit":
            print "service over , exit"
        elif instruction['cmd'] == "listen":
            print "listen"
            listen = mic.generalListen() # 注意threadhold设置
            print 'try to listen in handle and got ' + "#".join(listen)
            if listen != None :
                handle(text, mic, profile)
            else:
                mic.say("there is no answer. conversation over.")
        elif instruction['cmd'] == "sleep":
            print 'now to sleep for ', instruction['value'], ' seconds'
            time.sleep(int(instruction['value']))

def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    # return bool(re.search(u'状态', text, re.IGNORECASE))
    return True
