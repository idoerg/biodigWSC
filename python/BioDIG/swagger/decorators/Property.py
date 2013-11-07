#!usr/bin/python


def Properties(name, type):
    def inner(fn):
        fn.__name = name
        fn.__type = type
        return fn
    return inner

def Name(name):
    def inner(fn):
        fn.__name = name
        return fn
    return inner

def Type(type):
    def inner(fn):
        fn.__type = type
        return fn
    return inner

def Id(type, format):
    def inner(fn):
        fn.__type = type
        fn.__format = format
        return fn
    return inner

