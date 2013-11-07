#!usr/bin/python

##Decorators for the parameters
##Last edited By Dan Ruhe

##Function:Parameter
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_path(path, description):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
           
        fn.__operation.setDescription(Operation.desc)
        return fn
    return inner
##Function: Parameter Type query
##Use: Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
def ParamType_query(query):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setDescription(Operation.desc)
        return fn
    return inner
    
##Function:Parameter Type Body
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Body(body, description):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
        
        fn.__operation.setDescription(Operation.desc)
        return fn
    return inner
##Function: Parameter Type Form
##Use:##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Form(form, description):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
           
        fn.__operation.setDescription(Operation.desc)
        return fn
    return inner
    
##Function:Name
##Use:Defines what the name of the parameter block you are sending.
def Name(name):
    def inner(fn):
        fn.__name = name
        return fn
    return inner

##Function:Description
##Use:Describles the particular parameter
def Description(desc):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setDescription(Operation.desc)
        return fn
    return inner

##Function: Datatype parameter
##Use:Must be a primitive if the paramType is a path, query, or header
def Datatype(datatype):
    def inner(fn):
        fn.__datatype = datatype
        return fn
    return inner

##Function: Format of the API 
##Use: Determines if the format is an integer, double, string, etc.
def Format(APIformat):
    def inner(fn):
        fn.__APIformat = APIformat
        return fn

##Function: Required Parameter
##Use: Decorator for the required field, with the default being true
def required_true(required = True):
    def inner(fn):
        fn.__required = required
        return fn
    return inner


# The object for decorators looking for description
class Operation(object):
    def __init__(self):
        self.description = '' # default value for description

    def setDescription(self, desc):
        self.description = desc