'''
Created on Aug 21, 2017

@author: nsinha
'''

import datetime


class JSFile(object):
    """
    Javascript Model
    """

    _fname = None
    js = []
    jsvars = []
    jsfuncs = []

    def __init__(self, filename=None):
        """
        Construcutor
        """
        self._fname = filename
        self.jsfuncs = []

    def addJSFunc(self, name=None, params=None):
        """
        Adds a JS Function to JSFile and returns the object
        """
        jfunc = JSFunction(name=name, params=params)
        self.jsfuncs.append(jfunc)

        return jfunc

    def toString(self):
        """
        Generates Javascript String
        """
        strx = ""
        strx += "/*"
        strx += " This is an auto-generated file. Please use at your own risk \n"
        strx += " Do not modify the contents in this file as they shall get lost upon next code generation run.\n"
        strx += " Generated on: %s\n" % (datetime.datetime.now())
        strx += " \n"
        strx += "*/\n\n"

        for jsf in self.jsfuncs:
            strx += "//\n"
            strx += jsf.toString()
            strx += "\n"

        return strx


class JSFunction(object):
    """
    Javascript Function Model
    """

    _fname = None
    _body = []
    _params = []

    def __init__(self, name=None, params=None):
        """
        Constructor
        + name  : Name of the Javascript Function
        + params: Parameter list
        """
        self._fname = name
        self._params = params
        self._body = []

    def addParam(self, param):
        """
        Adds a param to the function model
        """
        if (param):
            self._params.append(param)

    def addBodyLine(self, line):
        """
        Adds a line to the function body
        """
        if (line):
            self._body.append(line)

    def addConsoleLog(self, line):
        """
        Adds a console.log statement 
        """
        if (line):
            self._body.append("console.log(" + line + ");")

    def addAlert(self, line):
        """
        Adds a console.log statement 
        """
        if (line):
            self._body.append("alert(" + line + ");")

    def addView(self, viewname=None):
        """
        """

    def toString(self):
        """
        String representation of the function body
        """
        strx = ""
        strx += "function %s (" % (self._fname)
        if (self._params):
            idx = 0
            for param in self._params:
                if idx > 0:
                    strx += ", "
                strx += param
                idx += 1

        strx += ") {\n"

        if (self._body):
            for line in self._body:
                strx += "\t%s\n" % (line)

        strx += "}\n"
        return strx


class JSClass(object):
    """
    Javascript Class
    """


class UIElement(object):
    '''
    classdocs
    '''

    def __init__(self, eltype, id=None):
        '''
        Constructor
        '''
