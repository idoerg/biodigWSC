#!usr/bin/python


def Properties(name, type):
    def inner(fn):
        fn.__name = name
        fn.__type = type
    return fn

def Name(name):
    def inner(fn):
        fn.__name = name
    return fn

def Type(type):
    def inner(fn):
        fn.__type = type
    return fn

def Id(type, format):
    def inner(fn):
        fn.__type = type
        fn.__format = format
    return fn

