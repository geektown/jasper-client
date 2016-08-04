# -*- coding: utf-8-*-
import urllib
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

WORDS = ["百科", "什么是"]

def getBaikeContent(item):
    print "baike query item = ", item
    url = "http://wapbaike.baidu.com/item/"+urllib.quote(item.encode('utf-8'))
    print url
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    html_soup = BeautifulSoup(content)
    summary = html_soup.findAll('div', class_='summary-content')
    
    result = u"没有找到百科上相关的知识，换一个试试吧！"
    # 按照句号进行分割，根据长度，拼接多个句子
    if len(summary) > 0:
        result = "为你找到百科" + item + "的概要内容："
        
        for pagraph in summary[0].getText().split(u'。'):
            result = result + "。" + pagraph.encode('utf-8').strip()
            if len(str(result)) > 1200:
                break
    print result, str(len(result))
    return result
    
def handle(text, mic, profile):
    item = text.replace(u'什么是','').replace(u"是什么", '').replace(u'？','').replace(u'开始检测 ','').replace(u'\n','')
    mic.say(getBaikeContent(item))




def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'什么', text, re.IGNORECASE))
