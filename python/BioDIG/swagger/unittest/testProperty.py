'''
Created on Nov 7, 2013

@author: Nguyen Ken
'''
#!/usr/bin/python
import unittest
import Types
import Property
from Property import Operation

class BioDIGtest(unittest.TestCase):
    def testProperty(self):
        @Property.Properties('name', Types.Integer)
        def testProperties():
            pass

        # test Property.Properties
        soln = [Operation.setName(self, 'name')]
        self.assertEqual(testProperties.__operation.description, soln)
        soln = [Operation.setType(self, Types.Integer)]
        self.assertEqual(testProperties.__operation.type, soln)


        @Property.Name('name')
        def testName():
            pass

        # test Property.Name
        soln = [Operation.setName(self, 'name')]
        self.assertEqual(testName.__operation.description, soln)

        @Property.Type(Types.Integer)
        def testType():
            pass

        # test Property.Type
        soln = [Operation.setType(self, Types.Integer)]
        self.assertEqual(testType.__operation.type, soln)

        @Property.Id(Types.Integer, 'int64')
        def testId():
            pass

        # test Property.Id
        soln = [Operation.setType(self, Types.Integer)]
        self.assertEqual(testId.__operation.type, soln)
        soln = [Operation.setFormat(self, 'int64')]
        self.assertEqual(testId.__operation.format, soln)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()