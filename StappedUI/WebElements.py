'''
Created on Aug 21, 2017

@author: nsinha
'''

import datetime
import lxml
from lxml.html import builder as HTM


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


class HtmlFile(object):
    """
    """

    html = None
    body = None
    head = None

    def __init__(self, appName):
        """
        HTML file
        """
        hx = '<html lang=\"en\">'
        hx += " <head>"
        hx += "   <title>" + appName + "</title>"
        hx += "   <meta charset=\"utf-8\">"
        hx += "   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        hx += '   <link href="https://fonts.googleapis.com/css?family=Indie+Flower|Lato|Oswald|Raleway|Roboto" rel="stylesheet">'
        hx += '   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
        hx += '   <link rel="stylesheet" href="css/app.css">'
        hx += '   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>'
        hx += '   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
        hx += '   <script src="js/bootstrapui.js"></script>'
        hx += '   <script src="js/app.js"></script>'
        hx += '   <script src="js/views.app.js"></script>'
        hx += ' </head>'
        hx += '<body>'
        hx += '  <div class="container" id="mcontent"></div>'
        hx += '  <div id="appmodal" class="modal fade" role="dialog"></div>'
        hx += '  <script>'
        hx += '    appInit();'
        hx += '  </script>'
        hx += '</body>'
        hx += '</html>'

        self.html = hx

    def getHTMLString(self):
        """
        """
        self.html


class UIElement(object):
    '''
    classdocs
    '''

    def __init__(self, eltype, id=None):
        '''
        Constructor
        '''
