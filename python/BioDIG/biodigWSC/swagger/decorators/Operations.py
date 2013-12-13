#!usr/bin/python

#For reference check the APIs section in API Declaration

###Includes the conversion for types

from DictDiffer import DictDiffer

# Constants for the Method Decorator
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

'''
   Sets the method being used one 4 HTTP methods.

   @param method The method to use GET, POST, PUT, DELETE
'''
def Method(method):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()

        fn.operations.setMethod(method)
        return fn
    return inner

'''
   Sets the nickname of the operations being described.
   This often corresponds to the method and the resource.
   For instance, a GET method with a type of Tag would usually
   revceive the nickname of "getTag".

   @param nickname The off-hand name for the operations.
'''
def Nickname(nickname):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()

        fn.operations.setNickname(nickname)
        return fn
    return inner

'''
    Sets the type returned by the operations. This type should be
    a primitive, which should be a constant from Types or an object
    annotated correctly using the Types decorators.

    @param obj The object/primitive returned by the operations
'''
def Type(obj):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()

        fn.operations.setObject(obj)
        return fn
    return inner

'''

'''
def Summary(summary):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()

        fn.operations.setSummary(summary)
        return fn
    return inner

def Notes(notes):
    def inner(fn):
        if not hasattr(fn, 'operations'):
            fn.operations = Operation()

        fn.operations.setNotes(notes)
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

        self.obj = None #default value for object

        self.params = { }

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

    def addParam(self, param):
        self.params[param.name] = param

    def getParam(self, name):
        try:
            return self.params[name]
        except KeyError:
            return None

    def __eq__(self, other):
        result = self.description == other.description and self.nickname == other.nickname and self.method == other.method and self.summary == other.summary and self.notes == other.notes and self.obj == other.obj
        result = result and len(DictDiffer(self.params, other.params).changed()) == 0
        return result