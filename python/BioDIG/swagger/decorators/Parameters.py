#!usr/bin/python

##Decorators for the parameters


    def paramType_path(fn, path)
       fn.__path = path
       return fn

    def paramType_query(fn, query)
       fn.__query = query
       return fn

    def paramType_body(fn, body)
       fn.__body = body
       return fn

    def paramType_form(fn, form)
       fn.__form = form
       return fn

    def name(fn, name)
       fn.__name = name
       return fn

    def description(fn, description)
       fn.__description = description
       return fn
    
    def datatype(fn, datatype)
       fn.__datatype = datatype
       return fn

    def format(fn, APIformat)
        fn.__APIformat = APIformat
        return fn

    ##Decorator for the required field being true
    def required_true(fn, required = true)
        fn.__required = required
        return fn

