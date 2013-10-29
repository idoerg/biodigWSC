#!usr/bin/python

##Hopefully the hierarchy of Properties was captured with that code.
def Properties(fn, name, type):
    fn.__name = name;
    fn.__type = type;
    return fn

def Name(fn, name):
    fn.__name = name;
    return fn

def Type(fn, type):
    fn.__type = type;
    return fn

def Id(fn, type, format):
    fn.__type = type;
    fn.__format = format;
    return fn

