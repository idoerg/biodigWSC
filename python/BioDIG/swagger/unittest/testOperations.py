'''
Created on Nov 7, 2013

@author: Nguyen Ken
'''
#!/usr/bin/python
import unittest
import Types
import Operations
from Operations import Operation

class BioDIGtest(unittest.TestCase):
    def testOperations(self):
        @Operations.Method('GET')
        def testMethod():
            pass

        # test Operations.Method
        soln = [Operation.setMethod(self, 'GET')]
        self.assertEqual(testMethod.__operation.method, soln)


        @Operations.Nickname('nickname')
        def testNickname():
            pass

        # test Operations.Nickname
        soln = [Operation.setNickname(self, 'nickname')]
        self.assertEqual(testNickname.__operation.nickname, soln)

        @Operations.Type(object)
        def testType():
            pass

        # test Operations.Type
        soln = [Operation.setObject(self, object)]
        self.assertEqual(testType.__operation.obj, soln)

        @Operations.Notes('notes')
        def testNotes():
            pass

        # test Operations.Notes
        soln = [Operation.setNotes(self, 'notes')]
        self.assertEqual(testNotes.__operation.type, soln)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()