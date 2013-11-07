#!usr/bin/python

#For reference see the API Declaration portion in the Swagger Specification

#Used to set the path of your API
def Path(path):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__operation.setPath(Operation.path)
        fn.__path = path;
        return fn
        
        return fn
    return inner

#Master description for your API
def Description(desc):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__operation.setDescription(Operation.desc)
        fn.__desc = desc;
        return fn
        
        
        return fn
    return inner

#Class for the variables and operations
class Operation(object):
    def __init__(self):
        
        self.path = '' #defualt values
        
        self.desc = '' #defualt values
        
        
    #Setters for the variables
    def setDescription(self, desc):
        self.description = desc
        
    def setPath(self, path):
        self.path = path