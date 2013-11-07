#!usr/bin/python

###Includes the conversion for types
String = 'string'
Boolean = 'boolean'
Date = 'date'
Integer = 'int'
dateTime = 'date-time'



def Name(name):
    def inner(fn):
        fn.__name = name
        return fn
    return inner


def DateCreated(dateCreated):
    def inner(fn):
        fn.__dateCreated = dateCreated
        return fn
    return inner

def Id(apiID):
    def inner(fn):
        fn.__apiID = apiID
        return fn
    return inner

def LastModified(lastModified):
    def inner(fn):
        fn.__lastModified = lastModified
        return fn
    return inner

def User(user):
    def inner(fn):
        fn._user = user
        return fn
    return inner

def IsPrivate(isPrivate = True):
    def inner(fn):
        fn.__isPrivate = isPrivate
        return fn
    return inner