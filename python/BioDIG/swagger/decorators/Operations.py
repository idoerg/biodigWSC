#!usr/bin/python

###Includes the conversion for types

def Method(method):
    def inner(fn):
        fn.__TagColor = method;
    return fn

##Requires the Tag class
def Nickname(Tag):
    def inner(fn):
        fn.__Tag = Tag.name;
    return fn

def Type(String):
    def inner(fn):
        fn.__String = String;
    return fn

def Summary(summary):
    def inner(fn):
        fn.__summary = summary;
    return fn

def Notes(notes):
    def inner(fn):
        fn.__notes = notes;
    return fn


