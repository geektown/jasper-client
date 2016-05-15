# -*- coding: utf-8-*-

import re

WORDS = ["等于"]



def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    print text
    # text = "开始检测 3+8-5等于几？"
    text = text[text.find(' ') + 1:] # 去掉空格前面的所有内容得到"3+8-5等于几？"，否则正则匹配不到，fixme
    print text
    pattern = re.compile('(\(*\d+(.\d+)*\)*(\+|-|x|÷|/|\*))+\d+(.\d+)*\)*')
    match = pattern.match(text)
    speech = "太难了，我算不出来。"
    if match:
        toBeCalc = match.group()
        print "toBeCalc ", toBeCalc
        answer = toBeCalc + "=" + str(eval(toBeCalc.decode('utf-8').replace(u'x','*').replace(u'÷','/')))
        print answer
        speech = answer.decode('utf-8').replace('+', u'加上').replace('-', u'减去').replace('x', u'乘以').replace(u'÷', u'除以').replace('=', u'等于')
        
        print speech
    mic.say(speech.encode('utf-8'))

def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(u'等于', text, re.IGNORECASE))
