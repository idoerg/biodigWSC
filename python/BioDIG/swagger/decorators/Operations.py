#!usr/bin/python

###Includes the conversion for types

def Method(fn,method):
    fn.__TagColor = method;
    return fn

##Requires the Tag class
def Nickname(fn, Tag):
    fn.__Tag = Tag.name;
    return fn

def Type(fn, String):
    fn.__String = String;
    return fn

def Summary(fn, summary):
    fn.__summary = summary;
    return fn

def Notes(fn, notes):
    fn.__notes = notes;
    return fn


