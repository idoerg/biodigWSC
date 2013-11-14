#!/usr/bin/python


##Used to import the Operations class and the methods there
import Operations
Operation = Operations.Operation()


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
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.addParam(Parameter(ParamType.PATH, name, description, dataType, form))

        return fn
    return inner

##Function: Parameter Type query
##Use: Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
def ParamType_Query(name, description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.addParam(Parameter(ParamType.QUERY, name, description, dataType, form))
        return fn
    return inner

##Function:Parameter Type Body
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Body(name, description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.addParam(Parameter(ParamType.BODY, name, description, dataType, form))
        return fn
    return inner
##Function: Parameter Type Form
##Use: Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Form(name, description='', dataType='', form=''):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.addParam(Parameter(ParamType.FORM, name, description, dataType, form))
        return fn
    return inner

##Function:Description
##Use:Describles the particular parameter, paired with name
def Description(name, desc):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        param = fn.__operation.getParameter(name)
        if not param:
            param = Parameter(name)

        param.setDescription(desc)

        return fn
    return inner

##Function: Datatype parameter
##Use:Must be a primitive if the paramType is a path, query, or header
def Datatype(dataType):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.setDatatype(dataType)
    return inner

##Function: Format of the API
##Use: Determines if the format is an integer, double, string, etc.
def Format(form):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.setFormat(form)
        return fn
    return inner

##Function: Required Parameter
##Use: Decorator for the required field, with the default being true
def required(required):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()

        fn.__parameter.setRequired(required)
        return fn
    return inner


# The object for decorators looking for description
class Parameter(object):
    def __init__(self):
        self.description = '' # default value for description

        self.required = True #defualt value for required

        self.format = '' #default value for format

        self.dataType = '' #default value for dataType

        self.name = '' #default value for name

        self.form = '' #default value for the form paramType

        self.body = '' #default value for the body ParamType

        self.query = '' #default value for the query ParamType

        self.path = '' #default value for the path ParamType

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

    def setParamType(self, param):
        self.param = param