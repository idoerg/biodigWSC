'''
Created on Nov 7, 2013

@author: Nguyen Ken
'''
#!/usr/bin/python
import unittest
import Types
import Parameters
from Parameters import Operation

class BioDIGtest(unittest.TestCase):
    def testParameters(self):
        @Parameters.ParamType_Path('path')
        def testParamType_Path():
            pass

        # test Parameters.ParamType_Path
        soln = [Operation.setParamType(self, 'path')]
        self.assertEqual(testParamType_Path.__operation.param, soln)


        @Parameters.ParamType_Query('query')
        def testParamType_Query():
            pass

        # test Parameters.ParamType_Query
        soln = [Operation.setParamType(self, 'query')]
        self.assertEqual(testParamType_Query.__operation.param, soln)

        @Parameters.ParamType_Body('body','description')
        def testParamType_Body():
            pass

        # test Parameters.ParamType_Body
        soln = [Operation.setParamType(self, 'body')]
        self.assertEqual(testParamType_Body.__operation.param, soln)
        soln = [Operation.setDescription(self, 'description')]
        self.assertEqual(testParamType_Body.__operation.description, soln)

        @Parameters.ParamType_Form('form')
        def testParamType_Form():
            pass

        # test Parameters.ParamType_Query
        soln = [Operation.setParamType(self, 'form')]
        self.assertEqual(testParamType_Form.__operation.param, soln)

        @Parameters.Name('name')
        def testName():
            pass

        soln = [Operation.setName(self, 'name')]
        self.assertEqual(testName.__operation.name, soln)

        @Parameters.Description('description')
        def testDescription():
            pass

        soln = [Operation.setDescription(self, 'description')]
        self.assertEqual(testDescription.__operation.description, soln)

        @Parameters.Datatype('dataType')
        def testDatatype():
            pass

        soln = [Operation.setDataType(self, 'dataType')]
        self.assertEqual(testDatatype.__operation.dataType, soln)

        @Parameters.Format('int64')
        def testFormat():
            pass
        soln = [Operation.setFormat(self, 'int64')]
        self.assertEqual(testFormat.__operation.format, soln)

        @Parameters.required(False)
        def testRequired():
            pass

        soln = [Operation.setRequired(self, False)]
        self.assertEqual(testRequired.__operation.required, soln)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()