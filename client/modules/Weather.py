# -*- coding: utf-8-*-
import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
from semantic.dates import DateService

# baidu apistore
import sys, urllib, urllib2, json
# WORDS = ["WEATHER", "TODAY", "TOMORROW"]
WORDS = ["天气", "今天", "明天", "温度"]



def handle(text, mic, profile):
    """
    使用baidu apistore 查询天气情况
    http://apistore.baidu.com/apiworks/servicedetail/112.html

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    
    url = 'http://apis.baidu.com/apistore/weatherservice/cityname?citypinyin=nanjing'
    req = urllib2.Request(url)
    req.add_header("apikey", "9306b0063beeaabe3d26f6561e34e546")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        print(content)
    data = json.loads(content)
    print data['errNum']
    print(data['retData']['city']) ## 南京
    print(data['retData']['weather']) ## 中雨
    print(data['retData']['temp']) ## 25
    print(data['retData']['l_tmp']) ## 16
    print(data['retData']['h_tmp']) ## 25
    print(data['retData']['WD']) ## 南风
    print(data['retData']['WS']) ## 10~17km/h
    
    print isinstance(data['retData']['city'], unicode)
    
    speechText = data['retData']['city'].encode('utf-8') + data['retData']['weather'].encode('utf-8')+ "，温度" + data['retData']['temp'].encode('utf-8') + "摄氏度。" + "最低温度" + data['retData']['l_tmp'].encode('utf-8') + "度。" + "最高温度" + data['retData']['h_tmp'].encode('utf-8') + "度。" + data['retData']['WD'].encode('utf-8')
    #   
    print(speechText)
    
    mic.say(speechText)


def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'天气', text, re.IGNORECASE))
