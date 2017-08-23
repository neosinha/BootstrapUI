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
    _css = None

    _staticDir = None

    def __init__(self, appName, staticDir):
        '''
        Constructor
        '''
        self._appname = appName
        self._staticDir = staticDir
        self.getFramework()
        self.initTemplate()
        self._html = HtmlFile(appName)
        self._css = []

    def initTemplate(self):
        """
        Initialize Template
        """

        # --- APP JS File
        self._jsFiles['app'] = JSFile('app')
        func = self._jsFiles['app'].addJSFunc(name="appInit", params=None)
        func.addConsoleLog("\"Hello word..\"")

        func = self._jsFiles['app'].addJSFunc(name="loginView", params=None)
        func.addConsoleLog("\"Login View controller\"")

        # -- View Controller File
        self._jsFiles['views'] = JSFile('views')

        # --

    def addCSSInclude(self, csspath=None):
        """
        Adds a CSS file to the current framework
        """
        self._html.includeCSS(csspath)

    def addJSInclude(self, jspath=None):
        """
        Adds a JS file to the current framework
        """
        self._html.includeJS(jspath)

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

    def writeHTML(self):
        """
        Write HTML
        """
        idxfile = os.path.join(self._staticDir, "index.html")
        fw = open(idxfile, 'w')
        print "Generating Index file, %s" % (fw.name)
        fw.write(self._html.getHTMLString())

    def write(self):
        """
        """
        self.writeHTML()
        self.writeJS()
