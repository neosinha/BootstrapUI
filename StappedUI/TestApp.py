'''
Created on Aug 22, 2017

@author: nsinha
'''
from UIApp import UIApp


class TestApp(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''


if __name__ == "__main__":
    uiapp = UIApp(appName="Test App",
                  staticDir="/Users/navendusinha/BootstrapUi/www")

    uiapp.addHeader(headerText="App1",
                    location={'filename': 'app',
                               'function': 'appInit'})

    uiapp.addView('view1')
    uiapp.write()
