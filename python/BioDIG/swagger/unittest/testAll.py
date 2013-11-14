'''
Created on Nov 14, 2013

@author: Nguyen Ken
'''
#!/usr/bin/python
import unittest
import Types
import Operations
import Model
import Parameters
import Applications
from Operations import Operation
from Model import Attribute
from Parameters import Parameter
from Applications import Application

class BioDIGtest(unittest.TestCase):
    '''
    testCases for Operations.py
    '''
    def testOperations(self):

        @Operations.Method(Operations.GET)
        def testMethod():
            pass

        # test Operations.Method
        soln = Operation()
        soln.setMethod(Operations.GET)
        self.assertEqual(testMethod.__operation, soln)

        @Operations.Nickname('nickname')
        def testNickname():
            pass

        soln = Operation()
        soln.setNickname('nickname')
        self.assertEqual(testNickname.__operation, soln)

        @Operations.Type('type')
        def testType():
            pass

        soln = Operation()
        soln.setObject('type')
        self.assertEqual(testType.__operation, soln)

        @Operations.Summary('summary')
        def testSummary():
            pass

        soln = Operation()
        soln.setSummary('summary')
        self.assertEqual(testSummary.__operation, soln)

        @Operations.Notes('notes')
        def testNotes():
            pass

        soln = Operation()
        soln.setNotes('notes')
        self.assertEqual(testNotes.__operation, soln)

    '''
    testCases for Model.py
    '''
    def testModel(self):
        @Model.Property('name', Types.String)
        def testProperty():
            pass

        soln = Attribute()
        soln.setName('name')
        soln.setType(Types.String)
        self.assertEqual(testProperty.__operation,soln)

        @Model.Name('name')
        def testName():
            pass

        soln = Attribute()
        soln.setName('name')
        self.assertEqual(testName.__operation,soln)

        @Model.Type(Types.String, 'name')
        def testType():
            pass

        soln = Attribute()
        soln.setType(Types.String)
        soln.setName('name')
        self.assertEqual(testType.__operation,soln)

        @Model.Id('name', 'tp' , None)
        def testId():
            pass

        soln = Model()
        soln.setType('tp')
        soln.setFormat(None)
        self.assertEqual(testId.__operation,soln)

    '''
    testCases for Parameters.py
    '''
    def testParameters(self):
        @Parameters.ParamType_Path('name')
        def testParamType_Path():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType.PATH)
        self.assertEqual(testParamType_Path.__operation,soln)

        @Parameters.ParamType_Query('name')
        def testParamType_Query():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType.QUERY)
        self.assertEqual(testParamType_Query.__operation,soln)

        @Parameters.ParamType_Body('name')
        def testParamType_Body():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType.BODY)
        self.assertEqual(testParamType_Body.__operation,soln)

        @Parameters.ParamType_Form('name')
        def testParamType_Form():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType.FORM)
        self.assertEqual(testParamType_Form.__operation,soln)

        @Parameters.Description('name', 'desc')
        def testDescription():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setDescription('desc')
        self.assertEqual(testDescription.__operation,soln)

        @Parameters.Datatype(Types.Integer)
        def testDataType():
            pass

        soln = Parameter()
        soln.setDataType(Types.Integer)
        self.assertEqual(testDataType.__operation,soln)

        @Parameters.Format('form')
        def testFormat():
            pass

        soln = Parameter()
        soln.setFormat('form')
        self.assertEqual(testFormat.__operation,soln)

        @Parameters.required(False)
        def testRequired():
            pass

        soln = Parameter()
        soln.setRequired(False)
        self.assertEqual(testRequired.__operation,soln)

    '''
    testCases for Applications.py
    '''
    def testApplication(self):
        @Applications.Path('path')
        def testPath():
            pass

        soln = Application()
        soln.setPath('path')
        self.assertEqual(testPath.__operation,soln)

        @Applications.Description('desc')
        def testAppDes():
            pass

        soln = Application()
        soln.setDescription('desc')
        self.assertEqual(testAppDes.__operation,soln)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()