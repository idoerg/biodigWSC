#!usr/bin/python

##Decorators for the parameters
##Last edited By Dan Ruhe

##Function:Parameter
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_path(path, description = ""):
    def inner(fn):
        if description == "":
            fn.__path = path
        else:
            fn.__path = description
        return fn
##Function: Parameter Type query
##Use: Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
def ParamType_query(query):
    def inner(fn):
        if fn.__description != null and fn.__description == Description.description:
           fn.__query = name
        else:
           fn.__name = "default name"
           fn.__query = name
        return fn
    
##Function:Parameter Type Body
##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Body(body, description = Description.description):
    def inner(fn):
        if description == Description.description:
            fn.__body = body
        else:
            fn.__body = description
        return fn
##Function: Parameter Type Form
##Use:##Use:Used to define the parameter type for the request. Will default if nothing is provided
def ParamType_Form(form, description = Description.description):
    def inner(fn):
        if description == Description.description:
           fn.__form = form
        else:
            fn.__form = description
        return fn
    
##Function:Name
##Use:Defines what the name of the parameter block you are sending.
def Name(name, description):
    def inner(fn):
        if name != "" or name != null:
           fn.__name = name
        else:
            fn.__name = description
        return fn

##Function:Description
##Use:Dexcribles the particular parameter
def Description(description):
    def inner(fn):
       fn.__description = description
       return fn

##Function: Datatype parameter
##Use:Must be a primitive if the paramType is a path, query, or header
def Datatype(datatype):
    def inner(fn):
       fn.__datatype = datatype
       return fn

##Function: Format of the API 
##Use: Determines if the format is an integer, double, string, etc.
def Format(APIformat):
    def inner(fn):
        fn.__APIformat = APIformat
        return fn

##Function: Required Parameter
##Use: Decorator for the required field, with the default being true
def required_true(required = true):
    def inner(fn):
        fn.__required = required
        return fn

