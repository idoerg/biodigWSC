#!usr/bin/python

###Includes the conversion for types
String = 'string'
Boolean = 'boolean'
Date = 'date'
Integer = 'int'
dateTime = 'date-time'


#####Decorators for Tags and Tag Groups
#####apiID, name overlaps with both Tags and Tag Groups
def Color(fn,TagColor):
    fn.__TagColor = TagColor
    return fn

def Name(fn, name):
    fn.__name = name
    return fn

def Point(fn, point):
    fn.__point = point
    return fn

def DateCreated(fn, dateCreated):
    fn.__dateCreated = dateCreated
    return fn

def Id(fn, apiID):
    fn.__apiID = apiID
    return fn


def ImageId(fn, imageid):
    fn.__imageid = imageid
    return fn

def LastModified(fn, lastModified):
    fn.__lastModified = lastModified
    return fn

def DateCreated(fn, dateCreated):
    fn.__dateCreated = dateCreated
    return fn

def User(fn, user):
    fn_user = user
    return fn

def IsPrivate(fn, isPrivate = true):
    fn.__isPrivate = isPrivate
    return fn
