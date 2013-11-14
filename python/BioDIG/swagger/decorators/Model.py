#!usr/bin/python

##Used to import the Operations class and the methods there
import Operations
Operation = Operations.Operation()

#This section was based off of the Swagger Specification of Data Types under the Complex Types section

#Decorator that is used when you define a more complex structure
def Property(name, typ):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__attribute.setName(name)
        fn.__name = name;
        
        fn.__attribute.setType(typ)
        fn.__typ = typ;
        return fn
    return inner

#Used to define the name
def Name(name):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__attribute.setName(name)
        fn.__name = name;
        return fn
    return inner

#Used to define the type of the function
def Type(tp, name):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operations.Operation()
            
        fn.__attribute.setName(name)
        fn.__type = type;
        return fn
    return inner

#Complex decorator that needs the name and the type
#tp == type, fm == format
def Id( name, tp, fm = None):
    def inner(fn):
        if not hasattr(fn, '__model'):
            fn.__model = Model()
            
        fn.__model.setType(tp)
        fn.__tp = tp;
        
        fn.__model.setFormat(fm)
        fn.__fm = fm;
        return fn
    return inner

class Model(object):
    def __init__(self):
        self.tp = {} # default value for tp(Type)
       
        self.fm = {} #default value for fm(format)
       
        self.name = {}

#Class of Objects for the decorators
class Attribute(object):
    def __init__(self):
        self.name = '' # default value for name
        
        self.typ = '' # default value for nickname
        
        self.summary = '' #default value for summary
        
        self.notes = '' #default value for notes
        
        self.object = None #default value for object

#Setters for the variables
    def setName(self, name):
        self.description = name
        
    def setNickname(self, nick):
        self.nickname = nick
        
    def setType(self, typ):
        self.typ = typ   
        
    def setObject(self, obj):
        self.obj= obj   
        
    def setSummary(self, summary):
        self.summary = summary  
        
    def setNotes(self, notes):
        self.notes = notes   