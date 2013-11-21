#!/usr/bin/python

#For reference see the API Declaration portion in the Swagger Specification

#Used to set the path of your API
def Path(path):
    def inner(fn):
        if not hasattr(fn, 'Application'):
            fn.application = Application()

        fn.application.setPath(path)
        fn.path = path;
        return fn

        return fn
    return inner

#Master description for your API
def Description(desc):
    def inner(fn):
        if not hasattr(fn, 'Application'):
            fn.application = Application()

        fn.application.setDescription(desc)
        fn.desc = desc;
        return fn


        return fn
    return inner

#Class for the variables and operations
class Application(object):
    def __init__(self):

        self.path = '' #default values

        self.desc = '' #default values


    #Setters for the variables
    def setDescription(self, desc):
        self.desc = desc

    def setPath(self, path):
        self.path = path

    def __eq__(self, other):
        return self.desc == other.desc and self.path == other.path