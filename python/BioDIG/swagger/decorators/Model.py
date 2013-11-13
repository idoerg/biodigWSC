#!usr/bin/python

#This section was based off of the Swagger Specification of Data Types under the Complex Types section

#Decorator that is used when you define a more complex structure
def Property(name, typ):
    def inner(fn):
        if not hasattr(fn, '__model'):
            fn.__model = Model()
            
        attribute = Attribute()
        attribute.setName(name)
        attribute.setType(typ)
        fn.__model.addAttribute(attribute)
        
        return fn
    return inner

#Used to define the name
def Description(desc):
    def inner(fn):
        if not hasattr(fn, '__model'):
            fn.__model = Model()
            
        fn.__model.setDescription(desc)
        return fn
    return inner

#Complex decorator that needs the name and the type
#tp == type, fm == format
def Id(ID):
    def inner(fn):
        if not hasattr(fn, '__model'):
            fn.__model = Model()
            
        fn.__model.setID(ID)
        return fn
    return inner

class Model(object):
    def __init__(self):
        self.ID = '' # default value for tp(Type)
       
        self.description = ''

        self.attributes = {}

    def setID(self, ID):
        self.ID = ID

    def setDescription(self, desc):
        self.description = desc

    def addAttribute(self, attr):
        self.attributes[attr.name] = attr

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
        self.name = name
        
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
