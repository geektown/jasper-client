# -*- coding: utf-8-*-
import unittest
import mock
import random
import json 

class TestGeneralConversation(unittest.TestCase):
    
 
    #def setUp(self):
        # print "setUp executing"
        
    #def tearDown(self):
        # print "tearDown executing"
        
    def getConversationFromFile(self):
        jsonFile = open("jasper-conversation.json", "r")
        conversation = list()
        for text in jsonFile.readlines():
            conversation.append(text)
        return conversation
        
    def test_tangshi_interaction(self):
        response = json.loads(self.getResponse())
        next = response["next"]
        while next != "finish":
            print('say or play ' + response["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
            if next == "activeListen":
                print "try to activeListen"
            else:
                print "say " + next.encode('utf-8')
            response = json.loads(self.getResponse())
            next = response["next"]
        print(response["say"].encode('utf-8')) + " ->>> and next is " + next.encode("utf-8")
        
    def getResponse(self):
        return random.choice(self.getConversationFromFile())
        
        
        
if __name__ == '__main__':
   unittest.main()            