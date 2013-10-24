#!usr/bin/python

##Decorators for the parameters
parameters = 
[
    
    def paramType_path(fn, path)
       fn_path = path
       return fn

    def paramType_query(fn, query)
       fn_query = query
       return fn

    def paramType_body(fn, body)
       fn_body = body
       return fn

    def paramType_form(fn, form)
       fn_form = form
       return fn

    def name(fn, name)
       fn_name = name
       return fn

    def description(fn, description)
       fn_description = description
       return fn
    
    def datatype(fn, datatype)
       fn_datatype = datatype
       return fn

    def format(fn, APIformat)
        fn_APIformat = APIformat
        return fn

    ##Decorator for the required field being true
    def required_true(fn, required)
        required = true
        fn_required = required
        return fn

    def required(fn, required)
        fn_required = required
        return fn
    
]
