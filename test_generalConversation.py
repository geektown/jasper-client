# -*- coding: utf-8-*-
import unittest
import os
import random
import json 
import time
from client import test_mic, diagnose, jasperpath
from client.modules import Life, Joke, Time, Gmail, HN, News, Weather, General

DEFAULT_PROFILE = {
    'prefers_email': False,
    'location': 'Cape Town',
    'timezone': 'US/Eastern',
    'phone_number': '012344321'
}

robotSay = [{"cmd":"say", "value":"唐诗已经找到，即将播放。"}, {"cmd":"sleep", "value":"3"}, {"cmd":"play", "value":"/home/pi/tangshi/05-5.mp3"}, {"cmd":"exit"}]

class TestGeneralConversation(unittest.TestCase):
    
    def setUp(self):
        self.profile = DEFAULT_PROFILE
        self.send = False
        
    def runConversation(self, query, inputs, module):
        """Generic method for spoofing conversation.

        Arguments:
        query -- The initial input to the server.
        inputs -- Additional input, if conversation is extended.

        Returns:
        The server's responses, in a list.
        """
        self.assertTrue(module.isValid(query))
        mic = test_mic.Mic(inputs)
        module.handle(query, mic, self.profile)
        return mic.outputs

    def testGeneralConversation(self):
        query = u"红烧肉怎么做？"
        inputs = []
        outputs = self.runConversation(query, inputs, General)
        print outputs

    def testTime(self):
        query = u"现在几点了？"
        inputs = []
        self.runConversation(query, inputs, Time)
              
        
if __name__ == '__main__':
   unittest.main()            