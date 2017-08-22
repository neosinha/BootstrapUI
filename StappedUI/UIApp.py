'''
Created on Aug 21, 2017

@author: nsinha
'''
from UIElements import JSFile, JSFunction
import os


class UIApp(object):
    '''
    classdocs
    '''

    _jsFiles = {}
    _html = None

    staticDir = None

    def __init__(self, appName, staticDir):
        '''
        Constructor
        '''
        self.addAppJS()

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

    def writeJS(self):
        """
        Write JS files
        """
        jsdir = os.path.join(self.staticDir, 'js')
        os.makedirs(jsdir)
        for jfname, jfile in self._jsFiles.iteritems():
            fw = open(os.path.join(jsdir, jfname + ".js"), 'w')
            fw.write(jfile.toString())

    def write(self):
        """
        """
        self.writeJS()


if __name__ == "__main__":
    uiapp = UIApp(appName="Test App",
                  staticDir="/Users/nsinha/git/BootstrapUI/www")
    uiapp.write()
