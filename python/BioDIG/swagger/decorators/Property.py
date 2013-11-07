#!usr/bin/python


def Properties(name, type):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setName(Operation.name)
        fn.__name = name;
        
        fn.__operation.setType(Operation.type)
        fn.__type = type;
        return fn
    return inner

def Name(name):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setName(Operation.name)
        fn.__name = name;
        return fn
    return inner

def Type(type):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setName(Operation.name)
        fn.__type = type;
        return fn
    return inner

def Id(type, format):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setType(Operation.type)
        fn.__type = type;
        
        fn.__operation.setFormat(Operation.format)
        fn.__format = format;
        return fn
    return inner


#Class of Objects for the decorators
class Operation(object):
    def __init__(self):
        self.name = '' # default value for name
        
        self.type = '' # default value for nickname
        
        self.summary = '' #default value for summary
        
        self.notes = '' #defualt value for notes
        
        self.object = None #default value for object

    def setDescription(self, desc):
        self.description = desc
        
    def setNickname(self, nick):
        self.nickname = nick
        
    def setType(self, type):
        self.type = type   
        
    def setObject(self, obj):
        self.obj= obj   
        
    def setSummary(self, summary):
        self.summary = summary  
        
    def setNotes(self, notes):
        self.notes = notes   