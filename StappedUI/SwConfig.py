"""
Module that contains all SWConfig Models

Created on Aug 28, 2017
@author: nsinha
"""

from lxml import etree
import os
import cherrypy as SWConfigServer
import argparse
import inspect
import re
import calendar
import time
import json


class CSDTag(object):
    """"
    """
    # CSD model related variables
    csddict = {}
    csddict['ConfigPartNum'] = None
    csddict['CSD_Name'] = None
    csddict['CSD_Version'] = 1

    csddict['ProductFamily'] = None
    csddict['SW_Version'] = None
    csddict['LicModel'] = 'SGEN'

    def __init__(self, configPartnum=None, csdName=None,
                 csdVersion=None, productFamily=None,
                 swVersion=None, licModel=None):
        """
        Initiallize CSDTag

        :param configPartnum
        :param csdName
        :param csdVersion
        :param productFamily
        :param swVersion
        :param licModel

        """
        self.addConfigPartNum(configPartnum)
        self.addCsdName(csdName)
        self.addCsdVersion(csdVersion)
        self.addProductFamily(productFamily)

    def addConfigPartNum(self, configPartnum):
        """
        Add ConfigPartnum 
        :param configPartnum
        """
        if configPartnum:
            self.csddict['ConfigPartNum'] = configPartnum

    def addCsdName(self, csdName):
        """
        Add CSD Name
        :param csdName
        """
        if csdName:
            self.csddict['CSD_Name'] = csdName

    def addCsdVersion(self, csdVersion):
        """
        Add CSD Version
        :param csdVersion
        """
        if csdVersion:
            self.csddict['CSD_Version'] = csdVersion

    def addProductFamily(self, productFamily):
        """
        Adds Product Family
        :param productFamily
        """
        if productFamily:
            self.csddict['ProductFamily'] = productFamily

    def addLicModel(self, licModel):
        """
        Adds Licence Model
        :param licModel
        """
        if licModel:
            self.csddict['LicModel'] = licModel

    def getDict(self):
        """
        Returns CSD Tag in Dictionary Format
        """
        return self.csddict

    def getXMLNode(self):
        """
        Returns XML Node
        """
        csdTag = etree.Element("CSD")
        csdTag.attrib['version'] = '3.1'

        for tag, value in self.csddict.iteritems():
            xmltag = etree.Element('tag')
            etree.SubElement(csdTag, tag).text = value
        return csdTag


class SwConfig(object):
    '''
    classdocs
    '''

    starttime = 0

    # XML related variables
    exportPath = None
    staticdir = None
    csdTag = None
    _softwarePartNum = None
    _swAttibutes = []

    def __init__(self, exportPath, staticdir):
        '''
        Constructor
        '''
        self.starttime = self.epoch()
        self.csdTag = CSDTag(configPartnum="51-1001888-01",
                             csdName="BROCADE CSD for 17r.1.00 on SLX9850-100GX12CQ-M",
                             csdVersion="3.0",
                             productFamily="SLX9850-100GX12CQ-M",
                             swVersion="17r.1.00",
                             licModel="SGEN")

        self.exportPath = exportPath
        self.staticdir = staticdir

        # self.xmlWriter()

    def epoch(self):
        """
         Returns the epoch
        """

        return int(calendar.timegm(time.gmtime()))

    @SWConfigServer.expose
    def csdSection(self, configPartnum="51-1001888-01",
                   csdName="BROCADE CSD for 17r.1.00 on SLX9850-100GX12CQ-M",
                   csdVersion="3.0",
                   productFamily="SLX9850-100GX12CQ-M",
                   swVersion="17r.1.00",
                   licModel="SGEN"):
        """
        CSD Section generator
        """

        self.csdTag = CSDTag(configPartnum="51-1001888-01",
                             csdName="BROCADE CSD for 17r.1.00 on SLX9850-100GX12CQ-M",
                             csdVersion="3.0",
                             productFamily="SLX9850-100GX12CQ-M",
                             swVersion="17r.1.00",
                             licModel="SGEN")

    @SWConfigServer.expose
    def xmlWriter(self):
        """
        Generates the XML file
        """
        if not os.path.exists(self.exportPath):
            os.makedirs(self.exportPath)
        xmlf = os.path.join(self.exportPath,
                            self.csdTag.getDict()['ConfigPartNum'])
        xml = file(xmlf, 'w')
        xml.write(etree.tostring(self.csdTag.getXMLNode()))

    @SWConfigServer.expose
    def index(self):
        """
        Implements the Index method
        """
        return open(os.path.join(self.staticdir, "index.html"))

    @SWConfigServer.expose
    def serverstatus(self):
        """
        Implements a status method
        """
        resp = {}
        resp['uptime'] = self.epoch() - self.starttime
        resp['epoch'] = self.starttime

        return json.dumps(resp)

    @SWConfigServer.expose
    def restapis(self):
        """
        """
        apis = {}
        dec_pattern = re.compile('@SWConfigServer')
        for name, mobj in inspect.getmembers(self):
            if inspect.ismethod(mobj):
                sourcelines = inspect.getsourcelines(mobj)
                decoratorLine = sourcelines[0][0]
                dec_match = dec_pattern.search(decoratorLine)
                if dec_match:
                    arglist = []
                    for argel in inspect.getargspec(mobj).args:
                        if argel.strip() != 'self':
                            arglist.append(argel)

                    apis[name] = {'module': mobj,
                                  'args': arglist
                                  }
        strxx = "%r" % (self.__class__)
        classname = "RestServer"
        strx = ""
        strx += "\nvar serverUrl=\"http://127.0.0.1:6500\";\n\n "
        strx += "\n/**"
        strx += "\n* RestAPIs defined by " + classname + ""
        strx += "\n* @class"
        strx += "\n* "
        strx += "\n**/"
        strx += "\nvar " + classname + " = function() {"
        for apiname, apiobj in apis.iteritems():
            strx += "\n\n"
            strx += "\n\t/**"
            doclinesx = inspect.getdoc(apiobj['module'])
            doclines = []
            if doclinesx:
                doclines = doclinesx.split('\n')
            apiobj['args'].append('callback')

            for docst in doclines:
                strx += "\n\t* " + docst
            strx += "\n\t* @method"
            strx += "\n\t* @memberof " + classname
            for p in apiobj['args']:
                if not p.startswith('self'):
                    strx += "\n\t* @param " + p + " - Parameter for " + p
            strx += "\n\t*"
            strx += "\n\t**/"
            strx += "\n\tthis." + apiname + " = function("
            pcount = 0
            for p in apiobj['args']:
                if not p.startswith('self'):
                    if pcount:
                        strx += ", "
                    strx += p
                    pcount = pcount + 1

            strx += ") {\n"
            strx += "\n\t\tvar urlx = serverUrl + '/" + apiname + "'"
            pcount = 0
            for p in apiobj['args']:
                if (not p.startswith('self')) & (not p.startswith('callback')):
                    if pcount == 0:
                        strx += "+'?'"
                    if pcount > 0:
                        strx += ";\n"
                        strx += "\t\turlx = urlx +'&'"
                    strx += "+'" + p + "='+" + p
                pcount += 1
            strx += ";\n"
            strx += "\n\n\t\t//AjaxCall \n"
            strx += "\t\tajaxLoad(callback, urlx);"
            strx += "\n\t};\n"
        strx += "\n}; "

        jsrest = os.path.join(self.staticdir, 'js')
        if not os.path.exists(jsrest):
            os.makedirs(jsrest)

        jsfile = os.path.join(jsrest, 'restapi.js')
        f = file(jsfile, 'w')
        f.write(strx)
        f.close()

        return strx

    @SWConfigServer.expose
    def restforms(self):
        """
        """
        apis = {}
        dec_pattern = re.compile('@SWConfigServer')
        for name, mobj in inspect.getmembers(self):
            if inspect.ismethod(mobj):
                sourcelines = inspect.getsourcelines(mobj)
                decoratorLine = sourcelines[0][0]
                dec_match = dec_pattern.search(decoratorLine)
                if dec_match:
                    arglist = []
                    for argel in inspect.getargspec(mobj).args:
                        if argel.strip() != 'self':
                            arglist.append(argel)

                    apis[name] = {'module': mobj,
                                  'args': arglist
                                  }
        strxx = "%r" % (self.__class__)
        classname = "RestForms"
        strx = ""
        # strx += "\nvar serverUrl=\"http://127.0.0.1:6500\";\n\n "
        strx += "\n/**"
        strx += "\n* RestForms defined by " + classname + ""
        strx += "\n* @class"
        strx += "\n* "
        strx += "\n**/"
        strx += "\nvar " + classname + " = function() {"
        for apiname, apiobj in apis.iteritems():
            if len(apiobj['args']) > 1:
                strx += "\n\n"
                strx += "\n\t/**"
                doclinesx = inspect.getdoc(apiobj['module'])
                doclines = []
                if doclinesx:
                    doclines = doclinesx.split('\n')

                for docst in doclines:
                    strx += "\n\t* " + docst
                    strx += "\n\t* @method"
                    strx += "\n\t* @memberof " + classname
                    # for p in apiobj['args']:
                    #    if not p.startswith('self'):
                    #        strx += "\n\t* @param " + p + " - Parameter for " + p
                strx += "\n\t*"
                strx += "\n\t**/"
                strx += "\n\tthis.get" + apiname.title() + " = function("
                strx += ") {\n"

                pcount = 0
                strx += "\t\tinpx = new Array();\n"
                strx += "\n"
                for p in apiobj['args']:
                    if not p.startswith('self'):
                        strx += "\n\t\t// Input Element for " + p + "\n"
                        strx += "\t\tinpx.push({ 'label' : \"" + p + "\", \n"
                        strx += "\t\t\t 'type' : \"text\", \n"
                        strx += "\t\t\t 'name' : '" + p + "', \n"
                        strx += "\t\t\t 'id' : '" + p + "', \n"
                        strx += "\t\t\t 'placeholder' : '" + \
                            p.title() + "'}); \n"
                        pcount = pcount + 1

                # strx += "\n\t\tvar urlx = serverUrl + '/" + apiname + "'"
                strx += "\n\t\tvar form = ui.createForm('form" + \
                    apiname.lower() + "', inpx); "
                strx += "\n\t\treturn form;"
                strx += "\n\t};\n"
                strx += "\n}; "

                jsrest = os.path.join(self.staticdir, 'js')
                if not os.path.exists(jsrest):
                    os.makedirs(jsrest)

                jsfile = os.path.join(jsrest, 'restforms.js')
                f = file(jsfile, 'w')
                f.write(strx)
                f.close()

        return strx


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
    SWConfigServer.config.update({'server.socket_host': ipadd,
                                  'server.socket_port': portnum,
                                  'server.socket_timeout': 600,
                                  'server.thread_pool': 8,
                                  'server.max_request_body_size': 0
                                  })
    print "Starting UI-HTTP Server on %s:%s" % (str(ipadd), str(portnum))

    SWConfigServer.quickstart(
        SwConfig(exportPath=os.path.join(staticdir, 'csd'),
                 staticdir=staticdir),
        '/', conf)

    # SwConfig("/Users/nsinha/Brocade/Extreme/CSD")
