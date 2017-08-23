'''
Created on Aug 21, 2017

@author: nsinha
'''
from WebElements import JSFile, JSFunction, HtmlFile
import os


class UIApp(object):
    '''
    classdocs
    '''

    _appname = None
    _jsFiles = {}
    _html = None

    _staticDir = None

    def __init__(self, appName, staticDir):
        '''
        Constructor
        '''
        self._appname = appName
        self._staticDir = staticDir
        self.getFramework()
        self.addAppJS()
        self._html = HtmlFile(appName)

    def addAppJS(self):
        """
        Adds app JS file
        """

        self._jsFiles['app'] = JSFile('app')

        func = self._jsFiles['app'].addJSFunc(name="appInit", params=None)
        func.addConsoleLog("\"Hello word..\"")

        func = self._jsFiles['app'].addJSFunc(name="loginView", params=None)
        func.addConsoleLog("\"Login View controller\"")

    def addView(self, viewname):
        """
        Adds an app View
        """

        return ""

    def getFramework(self):
        """
        Generates the boilerplate template
        """

    def writeJS(self):
        """
        Write JS files
        """
        jsdir = os.path.join(self._staticDir, 'js')
        # create JS directory if it does not exist
        if (not os.path.exists(jsdir)):
            os.makedirs(jsdir)

        for jfname, jfile in self._jsFiles.iteritems():
            fw = open(os.path.join(jsdir, ("%s.js" % (jfname))), 'w')
            print "Generating JS file, %s" % (fw.name)
            fw.write(jfile.toString())

    def write(self):
        """
        """
        self.writeJS()
