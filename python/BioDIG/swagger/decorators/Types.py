#!usr/bin/python

###Includes the conversion for types
String = 'string'
Boolean = 'boolean'
Date = 'date'
Integer = 'int'
dateTime = 'date-time'


#####Decorators for Tags and Tag Groups
#####apiID, name overlaps with both Tags and Tag Groups
def Color(TagColor):
    def inner(fn):
        fn.__TagColor = TagColor
    return fn

def Name(name):
    def inner(fn):
        fn.__name = name
    return fn

def Point(point):
    def inner(fn):
        fn.__point = point
    return fn

def DateCreated(dateCreated):
    def inner(fn):
        fn.__dateCreated = dateCreated
    return fn

def Id(apiID):
    def inner(fn):
        fn.__apiID = apiID
    return fn


def ImageId(imageid):
    def inner(fn):
        fn.__imageid = imageid
    return fn

def LastModified(lastModified):
    def inner(fn):
        fn.__lastModified = lastModified
    return fn

def DateCreated(dateCreated):
    def inner(fn):
        fn.__dateCreated = dateCreated
    return fn

def User(user):
    def inner(fn):
        fn_user = user
    return fn

def IsPrivate(isPrivate = true):
    def inner(fn):
        fn.__isPrivate = isPrivate
    return fn
