#!/usr/bin/env python2
# -*- coding: utf-8-*-
import unittest
from client import test_mic, diagnose, jasperpath
from client.modules import Time, Computer

DEFAULT_PROFILE = {
    'prefers_email': False,
    'location': 'Cape Town',
    'timezone': 'US/Eastern',
    'phone_number': '012344321'
}


class TestModules(unittest.TestCase):

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

    def testTime(self):
        query = u"现在几点了"
        inputs = []
        self.runConversation(query, inputs, Time)
        
    def test_wakeup_computer(self):
        query = u"开启服务器"
        inputs = []
        self.runConversation(query,inputs, Computer)
        for input in inputs:
            print input.decode('utf-8')
        
    def test_shutdown_computer(self):
        query = u"关闭服务器"
        inputs = []
        self.runConversation(query,inputs, Computer)
        for input in inputs:
            print input.decode('utf-8')

        
if __name__ == '__main__':
   unittest.main()      