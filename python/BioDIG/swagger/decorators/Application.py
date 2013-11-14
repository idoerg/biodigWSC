#!usr/bin/python

##Used to import the Operations class and the methods there
import Operations
Operation = Operations.Operation()

#For reference see the API Declaration portion in the Swagger Specification

#Used to set the path of your API
def Path(path):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__application.setPath(path)
        fn.__path = path;
        return fn
        
        return fn
    return inner

#Master description for your API
def Description(desc):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__application.setDescription(desc)
        fn.__desc = desc;
        return fn
        
        
        return fn
    return inner

#Class for the variables and operations
class Application(object):
    def __init__(self):
        
        self.path = '' #default values
        
        self.desc = '' #default values
        
        
    #Setters for the variables
    def setDescription(self, desc):
        self.description = desc
        
    def setPath(self, path):
        self.path = path