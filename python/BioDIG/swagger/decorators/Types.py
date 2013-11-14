#!usr/bin/python

import Operations
Operation = Operations.Operation()
#For reference see the Data Types section of the Swagger Specification

###Includes the conversion for types
String = 'string'
Boolean = 'boolean'
Date = 'date'
Integer = 'int'
dateTime = 'date-time'


#Sets the name of a Type
def Name(name):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__types.setName(Operation.name)
        fn.__name = name;
        return fn
    return inner

#Sets the ID of the type, 
def Id(ID):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__types.setID(Operation.ID)
        fn.__ID = ID;
        return fn
    return inner


#Sets the user property for the type
def User(user):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operations.Operation()  
            
        fn.__types.setUser(user)
        fn.__user = user;
        return fn
    return inner

#Will set the type's visibility property
def IsPrivate(isPrivate):
    def inner(fn):
        if not hasattr(fn, '__operation'):
            fn.__operation = Operation()  
            
        fn.__types.setisPrivate(isPrivate)
        fn.__isPrivate = isPrivate;
        return fn
    return inner


#####Group of Objects below here

# The object for decorators looking for description
class Types(object):
    def __init__(self):
        self.name = '' # default value for nickname
        
        self.ID = '' #default value for summary
        
        self.user = '' #default value for user
        
        self.isPrivate = True #default value for isPrivate

#Setters for the variables
    def setName(self, name):
        self.description = name
        
    def setID(self, ID):
        self.ID = ID   
        
    def setUser(self, user):
        self.user= user   
        
    def setIsPrivate(self, isPrivate):
        self.isPrivate = isPrivate   