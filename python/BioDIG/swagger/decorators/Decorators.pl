#!usr/bin/python

def Reponse (fn, code, message, responseModel):
        fn._code = code
        fn._message = message
        fn._responseModel = responseModel
        return fn
@basepath = ""
def bioDIGAPI (fn, address):
        fn._address = address
        return fn

@bioDIGAPI
@basepath = ""
def Tags (fn, ID, name, dateCreated, color, points):
        fn._ID = ID
        fn._name = name
        fn._dateCreated = dateCreated
        fn._color = color
        fn._points = points
        return fn

@bioDIGAPI
@basepath = ""
def geneLinks (fn, ID, tagID, uniquename, name, organismID):
        fn._ID = ID
        fn._tagID = tagID
        fn._uniquename = uniquename
        fn._name = name
        fn._organismID = organismID
        return fn

@bioDIGAPI
@basepath = ""
def TagGroup(fn, ID, imageID, lastModified, dateCreated, name, user, isPrivate):
        return fn