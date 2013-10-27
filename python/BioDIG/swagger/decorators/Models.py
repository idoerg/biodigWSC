#!usr/bin/python

#####Decorators for Tags and Tag Groups
#####apiID, name overlaps with both Tags and Tag Groups
def Property_color(fn,TagColor)
    fn.__TagColor = TagColor
    return fn

def Property_name(fn, name)
    fn.__name = name
    return fn

def Property_point(fn, point)
    fn.__point = point
    return fn

def Property_dateCreated(fn, dateCreated)
    fn.__dateCreated = dateCreated
    return fn

def Property_id(fn, apiID)
    fn.__apiID = apiID
    return fn


def Property_imageid(fn, imageid)
    fn.__imageid = imageid
    return fn

def Property_lastModified(fn, lastModified)
    fn.__lastModified = lastModified
    return fn

def Property_dateCreated(fn, dateCreated)
    fn.__dateCreated = dateCreated
    return fn

def Property_user(fn, user)
    fn_user = user
    return fn

def Property_isPrivate(fn, isPrivate = true)
    fn.__isPrivate = isPrivate
    return fn