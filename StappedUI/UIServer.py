'''
Created on Aug 21, 2017

@author: nsinha
'''

import cherrypy as UIServer
import calendar
import time
import json
import os
import argparse
import inspect
import re


class UIServerlet(object):
    '''
    classdocs
    '''

    www = None
    dbaddress = None
    starttime = 0

    def __init__(self, dbaddress="10.30.5.203:27017", www=None):
        '''
        UIServer Class
        '''
        self.starttime = self.epoch()
        self.dbaddress = dbaddress
        self.www = www

    def epoch(self):
        """
        Returns the epoch
        """

        return int(calendar.timegm(time.gmtime()))

    @UIServer.expose
    def serverstatus(self):
        """
        Returns the server status.. 
        A good test API
        """
        resp = {}
        resp['uptime'] = self.epoch() - self.starttime
        resp['epoch'] = self.starttime

        return json.dumps(resp)

    @UIServer.expose
    def index(self):
        """
        Serves the index page
        """
        return open(os.path.join(self.www, "index.html"))

    @UIServer.expose
    def echo(self, param1, param2):
        """
        Test echo function
        """
        resp = {"el1": param1, "el2": param2}

        return json.dumps(resp)

    @UIServer.expose
    def inspect(self):
        """
        """
        apis = {}
        dec_pattern = re.compile('@UIServer')
        for name, mobj in inspect.getmembers(self):
            if inspect.ismethod(mobj):
                sourcelines = inspect.getsourcelines(mobj)
                decoratorLine = sourcelines[0][0]
                dec_match = dec_pattern.search(decoratorLine)
                if dec_match:
                    apis[name] = {'module': mobj,
                                  'args': inspect.getargspec(mobj).args
                                  }

if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--port", required=True,
                    help="Port number to start HTTPServer")

    ap.add_argument("-i", "--ipaddress", required=True,
                    help="IP Address to start HTTPServer")

    ap.add_argument("-d", "--mongo", required=True,
                    help="IP Address for MongoDB server")

    ap.add_argument("-w", "--staticdir", required=True,
                    help="Static directory which contains the WWW folder")

    args = vars(ap.parse_args())
    portnum = int(args["port"])
    ipadd = args["ipaddress"]
    dbadd = args["mongo"]
    staticdir = args["staticdir"]

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': staticdir
        }
    }
    UIServer.config.update({'server.socket_host': ipadd,
                            'server.socket_port': portnum,
                            'server.socket_timeout': 600,
                            'server.thread_pool': 4,
                            'server.max_request_body_size': 0
                            })
    print "Starting UI-HTTP Server on %s:%s" % (str(ipadd), str(portnum))

    UIServer.quickstart(
        UIServerlet(dbaddress="127.0.0.1", www=staticdir),
        '/', conf)
