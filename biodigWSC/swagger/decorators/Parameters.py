#!usr/bin/python


##Used to import the Operations class and the methods there
from Operations import Operation


##Decorators for the parameters
##See the Parameters section in the Swagger Specification
##Last edited By Dan Ruhe

ParamType = {
    'PATH' : 'path',
    'QUERY' : 'query',
    'HEADER' : 'header',
    'FORM' : 'form',
    'BODY' : 'body'
}

##Function:Parameter
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Path(name, description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()
        paramType = ParamType['PATH']   
        fn.operations.addParam(Parameter(name, paramType, description, dataType, form))
        
        return fn
    return inner
##Function: Parameter Type query
##Use: Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
def ParamType_Query(name, paramType='', description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()
        paramType = ParamType['QUERY']   
        fn.operations.addParam(Parameter(name, paramType, description, dataType, form))
        return fn
    return inner
    
##Function:Parameter Type Body
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Body(name, paramType='', description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()
        paramType = ParamType['BODY']
        fn.operations.addParam(Parameter(name, paramType, description, dataType, form))
        return fn
    return inner
##Function: Parameter Type Form
##Use: Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Form(name, paramType='', description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()
        paramType = ParamType['FORM']    
        fn.operations.addParam(Parameter(name, paramType, description, dataType, form))
        return fn
    return inner
    
##Function:Description
##Use:Describles the particular parameter, paired with name
def Description(name, desc):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()   
            
        param = fn.operations.getParam(name)
        if not param:
            param = Parameter(name)

        param.setDescription(desc)
        fn.operations.addParam(param)
        
        return fn
    return inner

##Function: Datatype parameter
##Use:Must be a primitive if the paramType is a path, query, or header
def Datatype(name, dataType):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()   
            
        param = fn.operations.getParam(name)
        if not param:
            param = Parameter(name)

        param.setDataType(dataType)
        fn.operations.addParam(param)
        
        return fn
    return inner

##Function: Format of the API 
##Use: Determines if the format is an integer, double, string, etc.
def Format(name, form):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()   
            
        param = fn.operations.getParam(name)
        if not param:
            param = Parameter(name)

        param.setFormat(form)
        fn.operations.addParam(param)
        
        return fn
    return inner

##Function: Required Parameter
##Use: Decorator for the required field, with the default being true
def required(name, required):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()   
            
        param = fn.operations.getParam(name)
        if not param:
            param = Parameter(name)

        param.setRequired(required)
        fn.operations.addParam(param)
        
        return fn
    return inner


# The object for decorators looking for description
class Parameter(object):
    def __init__(self, name='', paramType='', description='', dataType='', form=''):
        self.description = description # default value for description

        self.required = True #default value for required

        self.form = form #default value for format

        self.dataType = dataType #default value for dataType
        
        self.name = name #default value for name
       
        self.param = {} #dictionary variable to hold the different parameters
        
        self.paramType = paramType #default vale for a paramType

        
       

#Setters for the variables above
    def setDescription(self, desc):
        self.description = desc
        
    def setName(self, name):
        self.name = name
        
    def setFormat(self, form):
        self.form = form   
    
    def setRequired(self, required):
        self.required = required
        
    def setDataType(self, dataType):
        self.dataType = dataType   
        
    def setParamType(self, paramType):
        self.paramType = paramType   
        
    def __eq__(self, other): 
        return self.description == other.description and self.name == other.name and self.form == other.form and self.required == other.required and self. dataType == other.dataType   