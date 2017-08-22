'''
Created on Aug 21, 2017

@author: nsinha
'''
from UIElements import JSFile, JSFunction


class UIApp(object):
    '''
    classdocs
    '''

    _jsFile = None
    _html = None

    def __init__(self, appName):
        '''
        Constructor
        '''
        self._jsFile = JSFile('app')

        func = self._jsFile.addJSFunc(name="appInit", params=None)
        func.addConsoleLog("\"Hello word..\"")

        func = self._jsFile.addJSFunc(name="loginView", params=None)

        print "==> %s" % (self._jsFile.toString())


if __name__ == "__main__":
    uiapp = UIApp("Test App")
