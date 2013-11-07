#!usr/bin/python

##Decorators for the parameters
##See the Parameters section in the Swagger Specification
##Last edited By Dan Ruhe

##Function:Parameter
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Path(path):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
           
        if(path == '' and Operation.name != ''):    
            fn.__operation.setParamType(Operation.name)
        else:    
            fn.__operation.setParamType(Operation.path)
        return fn
    return inner
##Function: Parameter Type query
##Use: Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
def ParamType_Query(query):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        if(query == '' and Operation.name != ''):    
            fn.__operation.setParamType(Operation.name)
        else:    
            fn.__operation.setParamType(Operation.query)
        return fn
    return inner
    
##Function:Parameter Type Body
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Body(body, description):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
        
        if(body == '' and Operation.name != ''):    
            fn.__operation.setParamType(Operation.name)
        else:    
            fn.__operation.setParamType(Operation.body)
        return fn
    return inner
##Function: Parameter Type Form
##Use: Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Form(form):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
           
        if(form == '' and Operation.name != ''):    
            fn.__operation.setParamType(Operation.name)
        else:    
            fn.__operation.setParamType(Operation.form)
        return fn
    return inner
    
##Function:Name
##Use:Defines what the name of the parameter block you are sending.
def Name(name):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setName(Operation.name)
    return inner

##Function:Description
##Use:Describles the particular parameter, paired with name
def Description(desc):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
            
        if(desc == ''):    
            fn.__operation.setDescription(Operation.name)
        else:
            fn.__operation.setDescription(Operation.desc)
        return fn
    return inner

##Function: Datatype parameter
##Use:Must be a primitive if the paramType is a path, query, or header
def Datatype(datatype):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setDatatype(Operation.dataType)
    return inner

##Function: Format of the API 
##Use: Determines if the format is an integer, double, string, etc.
def Format(format):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setFormat(Operation.format)
        return fn
    return inner

##Function: Required Parameter
##Use: Decorator for the required field, with the default being true
def required(required):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setRequired(Operation.required)
        return fn
    return inner


# The object for decorators looking for description
class Operation(object):
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

    def setDescription(self, desc):
        self.description = desc
        
    def setName(self, name):
        self.name = name
        
    def setForm(self, form):
        self.form = form   
    
    def setRequired(self, required):
        self.required = required
        
    def setDataType(self, dataType):
        self.dataType = dataType    
        
    def setParamType(self, param):
        self.param = param