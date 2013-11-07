#!usr/bin/python

###Includes the conversion for types

def Method(method):
    def inner(fn):
        fn.__method = method;
        return fn
    return inner

##Requires the Tag class
def Nickname(nickname):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()
            
        fn.__operation.setDescription(Operation.desc)
        fn.__nickname = nickname;
        return fn
    return inner

def Type(object):
    def inner(fn):
        fn.__object = object;
        return fn
    return inner

def Summary(summary):
    def inner(fn):
        fn.__summary = summary;
        return fn
    return inner

def Notes(notes):
    def inner(fn):
        fn.__notes = notes;
        return fn
    return inner

# The object for decorators looking for description
class Operation(object):
    def __init__(self):
        self.description = '' # default value for description

    def setDescription(self, desc):
        self.description = desc