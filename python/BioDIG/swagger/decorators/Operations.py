#!usr/bin/python


#For reference check the APIs section in API Declaration

###Includes the conversion for types

def Method(method):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setMethod(method)
        return fn
    return inner

##Requires the Tag class
def Nickname(nickname):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setNickname(nickname)
        return fn
    return inner


def Type(obj):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setObject(obj)
        return fn
    return inner

def Summary(summary):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setSummary(summary)
        return fn
    return inner

def Notes(notes):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__operation.setNotes(notes)
        return fn
    return inner


#####Group of Objects below here

# The object for decorators looking for description
class Operation(object):
    def __init__(self):
        self.description = '' # default value for description
        
        self.nickname = '' # default value for nickname
        
        self.method = None #default value for method
        
        self.summary = '' #default value for summary
        
        self.notes = '' #defualt value for notes
        
        self.object = None #default value for object

    def setDescription(self, desc):
        self.description = desc
        
    def setNickname(self, nick):
        self.nickname = nick
        
    def setMethod(self, method):
        self.method = method   
        
    def setObject(self, obj):
        self.obj= obj   
        
    def setSummary(self, summary):
        self.summary = summary  
        
    def setNotes(self, notes):
        self.notes = notes   
