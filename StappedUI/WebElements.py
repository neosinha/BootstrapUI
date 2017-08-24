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
    bodyLines = []

    def __init__(self, filename=None):
        """
        Construcutor
        """
        self._fname = filename
        self.jsfuncs = []
        self.bodyLines = []

    def addJSFunc(self, name=None, params=None):
        """
        Adds a JS Function to JSFile and returns the object
        """
        jfunc = JSFunction(name=name, params=params)
        self.jsfuncs.append(jfunc)

        return jfunc

    def getJSFunc(self, name):
        """
        Returns JS Function matching name 
        + name : 
        """
        jf = None
        for jfunc in self.jsfuncs:
            if (jfunc.getName() == name):
                jf = jfunc
                break
        return jf

    def addBodyLine(self, line):
        """
        Adds a line to the JS file
        """
        if (line):
            self.bodyLines.append(line.strip())

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

        for line in self.bodyLines:
            strx += line + "\n"

        strx += "\n\n"

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

    def getName(self):
        """
        Returns the function name
        """
        return self._fname

    def getParams(self):
        """
        Returns the function parameters
        """
        return self._params

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
    headTitle = None
    headFoot = None
    body = None
    css = None
    js = None

    cssDef = None
    jsDef = None

    def __init__(self, appName):
        """
        HTML file
        """

        self.cssDef = []
        self.jsDef = []

        self.headTitle = " <head>"
        self.headTitle += "   <title>" + appName + "</title>"
        self.headTitle += "   <meta charset=\"utf-8\">"
        self.headTitle += "   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"

        self.css = '   <link href="https://fonts.googleapis.com/css?family=Indie+Flower|Lato|Oswald|Raleway|Roboto" rel="stylesheet">'
        self.css += '   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'

        self.js = '   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>'
        self.js += '   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
        self.js += '   <script src="https://api.sinhallc.com/bootstrapui/bootstrapui.js"></script>'
        self.js += '   <script src="js/app.js"></script>'
        self.js += '   <script src="js/views.js"></script>'

        self.body = '<body>'
        self.body += '  <div class="container" id="mcontent"></div>'
        self.body += '  <div id="appmodal" class="modal fade" role="dialog"></div>'
        self.body += '  <script>'
        self.body += '    appInit();'
        self.body += '  </script>'
        self.body += '</body>'

    def includeCSS(self, cssPath):
        """
        Generates an include for the CSS Path defined in cssPath
        """
        if cssPath:
            self.cssDef.append(cssPath)

    def includeJS(self, jsPath):
        """
        Generates an include for the JS file defined in jsPath
        """
        if jsPath:
            self.jsDef.append(jsPath)

    def getHTMLString(self):
        """
        Genertes the HTML Page String
        """
        self.html = '<html lang=\"en\">'
        self.html += self.headTitle
        for css in self.cssDef:
            self.css += '   <link rel="stylesheet" href=' + css + '">'

        self.html += self.css

        for js in self.jsDef:
            self.js += '   <script src=' + js + '></script>'

        self.html += self.js

        # Add the HTML body
        self.html += self.body

        # Close the HTML tag
        self.html += '</html>'

        return self.html


class UIElement(object):
    '''
    classdocs
    '''

    def __init__(self, eltype, id=None):
        '''
        Constructor
        '''
