#!/usr/bin/env python
# encoding: utf-8
'''
OptParseTest -- shortdesc

OptParseTest is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2013 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import imp

from optparse import OptionParser

__all__ = []
__version__ = 0.1
__date__ = '2013-11-18'
__updated__ = '2013-11-18'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    #program_usage = '''usage: spam two eggs''' # optional - will be autogenerated by optparse
    program_longdesc = '''''' # optional - give further explanation about what the program does
    program_license = "Copyright 2013 user_name (organization_name)                                            \
                Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"

    if argv is None:
        argv = sys.argv[0:]

    # setup option parser
    #add operation spec, model spec, and application spec
    #check to see if the files can be loaded, (How to import a file given the full path)

    #import imp
    #foo= imp.load_source('module.name', '/path/to/file.py')
    #foo.MyClass()
    parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
    #parser.add_option("-i", "--in", dest="infile", help="set input path [default: %default]", metavar="FILE")
#    parser.add_option("-o", "--out", dest="outfile", help="set output path [default: %default]", metavar="FILE")
    parser.add_option("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: 1]", default=2)
    #parser.add_option("-f", "--file", dest="outfile", action="store", help="write report to FILE", metavar="FILE")
    #parser.add_option("-p", "--path", dest="paths", help="Set directory for Decorators", metavar="FILE", default="")
    #Operations to handle the files for the optparser
    parser.add_option("-o", "--operations", dest="operations", help="Sets the file path for the operations file", metavar="FILE", default='./Operations.py')
    parser.add_option("-m", "--models", dest="models", help="Sets the file path for the models file", metavar="FILE", default='./Models.py')
    parser.add_option("-a", "--appications", dest="applications", help="Sets the file path for the applications file", metavar="FILE",default='./Applications.py')
    parser.add_option("-p", "--parameters", dest="parameters", help="Sets the file path for the parameter file", metavar="FILE",default='./Parameters.py')

    # set defaults, add logic to see if there are no defaults, throw an exception
    #parser.set_defaults(operations="out.txt", models="in.txt", applications="")

    # process options
    # Ask for optional custom directory
    (opts, args) = parser.parse_args()
    if opts.operations == "./Operations.py":
        temp = raw_input("Please specify the location of Operations Module (Default: current directory): ")
        if temp != "":
            opts.operations = temp

    if opts.models == "./Models.py":
        temp = raw_input("Please specify the location of Models Module (Default: current directory): ")
        if temp != "":
            opts.models = temp

    if opts.applications == "./Applications.py":
        temp = raw_input("Please specify the location of Applications Module (Default: current directory): ")
        if temp != "":
            opts.applications = temp

    if opts.parameters == "./Parameters.py":
        temp = raw_input("Please specify the location of Parameters Module (Default: current directory): ")
        if temp != "":
            opts.parameters = temp


# MAIN BODY #
    #print opts.operations
    #Operations logic
    Operations = imp.load_source('Operations', opts.operations)

    #Models logic
    Models = imp.load_source('Models', opts.models)

    #Applications logic
    Applications = imp.load_source('Applications', opts.applications)

    #Parameters logic
    Parameters = imp.load_source('Parameters', opts.parameters)

    if opts.verbose == 2:
        print "\n"
        #List Object inside Operations
        print "___Operations structure___\n"
        for i in dir(Operations):
            print i,"  ",type(getattr(Operations,i))

        print "\n\n"
        #List Object inside Operations
        print "___Models structure___\n"
        for i in dir(Models):
            print i,"  ",type(getattr(Models,i))

        print "\n\n"
        #List Object inside Operations
        print "___Applications structure___\n"
        for i in dir(Applications):
            print i,"  ",type(getattr(Applications,i))

        print "\n\n"
        #List Object inside Operations
        print "___Parameters structure___\n"
        for i in dir(Parameters):
            print i,"  ",type(getattr(Parameters,i))


if __name__ == "__main__":
    if DEBUG:
        sys.argv.append(raw_input())
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'OptParseTest_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())