#!usr/bin/python

##Decorators for the parameters


    def paramType_path(fn, path, description = ""):
	if( description == "")
	{
       fn.__path = path;
       return fn
	}
	else
	{
	fn.__path = description;
	return fn
	}
	   ###Has logic to determine if the name value has been populated. Will enter a default name if it has not, will preserve if it has
    def paramType_query(fn, query):
	if(fn.__description =! null and fn.__description == Description.description)
	{
       fn.__query = name;
       return fn
	}
	   else
	{
	   fn.__name = "default name"
	   fn.__query = name;
       return fn
	}

    def paramType_Body(fn, body):
       fn.__body = body;
       return fn

    def paramType_Form(fn, form):
       fn.__form = form;
       return fn

    def Name(fn, name, description):
	if (name != "") or (name != null)
	{
       fn.__name = name;
	   return fn
	}
	else
	{
	 fn.__name = description
     return fn
	}

    def Description(fn, description):
       fn.__description = description;
       return fn
    
    def Datatype(fn, datatype):
       fn.__datatype = datatype;
       return fn

    def Format(fn, APIformat):
        fn.__APIformat = APIformat;
        return fn

    ##Decorator for the required field default being true
    def required_true(fn, required = true):
        fn.__required = required;
        return fn

