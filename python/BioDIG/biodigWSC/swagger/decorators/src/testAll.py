'''
Created on Nov 14, 2013

@author: Nguyen Ken
'''
#!/usr/bin/python
import unittest
import Types
import Operations
import Models
import Parameters
import Applications
from Operations import Operation
from Models import Attribute, Model
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
        self.assertEqual(testMethod.operation, soln)

        @Operations.Nickname('nickname')
        def testNickname():
            pass

        soln = Operation()
        soln.setNickname('nickname')
        self.assertEqual(testNickname.operation, soln)

        @Operations.Type('type')
        def testType():
            pass

        soln = Operation()
        soln.setObject('type')
        self.assertEqual(testType.operation, soln)

        @Operations.Summary('summary')
        def testSummary():
            pass

        soln = Operation()
        soln.setSummary('summary')
        self.assertEqual(testSummary.operation, soln)

        @Operations.Notes('notes')
        def testNotes():
            pass

        soln = Operation()
        soln.setNotes('notes')
        self.assertEqual(testNotes.operation, soln)

    '''
    testCases for Model.py
    '''
    def testModel(self):
        @Models.Property('name', Types.String)
        def testProperty():
            pass

        soln = Attribute()
        soln.setName('name')
        soln.setType(Types.String)
        self.assertEqual(testProperty.model.attributes['name'],soln)


        @Models.Id('id')
        def testId():
            pass

        soln = Model()
        soln.setID('id')
        self.assertEqual(testId.model,soln)

    '''
    testCases for Parameters.py
    '''
    def testParameters(self):
        @Parameters.ParamType_Path('name')
        def testParamType_Path():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType['PATH'])
        self.assertEqual(testParamType_Path.operations.getParam('name'),soln)

        @Parameters.ParamType_Query('name')
        def testParamType_Query():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType['QUERY'])
        self.assertEqual(testParamType_Query.operations.getParam('name'),soln)

        @Parameters.ParamType_Body('name')
        def testParamType_Body():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType['BODY'])
        self.assertEqual(testParamType_Body.operations.getParam('name'),soln)

        @Parameters.ParamType_Form('name')
        def testParamType_Form():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setParamType(Parameters.ParamType['FORM'])
        self.assertEqual(testParamType_Form.operations.getParam('name'),soln)

        @Parameters.Description('name', 'desc')
        def testDescription():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setDescription('desc')
        self.assertEqual(testDescription.operations.getParam('name'),soln)

        @Parameters.Datatype('name', Types.Integer)
        def testDataType():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setDataType(Types.Integer)
        self.assertEqual(testDataType.operations.getParam('name'),soln)

        @Parameters.Format('name', 'form')
        def testFormat():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setFormat('form')
        self.assertEqual(testFormat.operations.getParam('name'),soln)

        @Parameters.required('name', False)
        def testRequired():
            pass

        soln = Parameter()
        soln.setName('name')
        soln.setRequired(False)
        self.assertEqual(testRequired.operations.getParam('name'),soln)

    '''
    testCases for Applications.py
    '''
    def testApplication(self):
        @Applications.Path('path')
        def testPath():
            pass

        soln = Application()
        soln.setPath('path')
        self.assertEqual(testPath.application,soln)

        @Applications.Description('desc')
        def testAppDes():
            pass

        soln = Application()
        soln.setDescription('desc')
        self.assertEqual(testAppDes.application,soln)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
