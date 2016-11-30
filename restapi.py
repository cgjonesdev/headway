import os
from pprint import pprint, pformat
import requests


class RestAPI(object):
    base_url = 'http://localhost'
    port = ':8081'

    def __init__(self):
        try:
            response = requests.get(self.base_url + self.port)
            if response.text == 'ERROR':
                raise Exception('API has not been unlocked')
        except:
            unlock_file_loc = 'xmlpublisher/Xojo/Testing/unlockTestAPI.command'
            if os.path.isfile(unlock_file_loc):
                os.system(unlock_file_loc)
        finally:
            print '\n'

    @property
    def toc(self):
        response = requests.get(self.base_url + self.port + '/toc')
        return response.text

    def fileExists(self, file):
        response = requests.get(
            self.base_url + self.port + '/fileExists/file%3A%2F%2F%2F{}'.format(
                file))
        return response.text

    def getFile(self, file):
        response = requests.get(
            self.base_url + self.port + '/getFile/file%3A%2F%2F%2F{}'.format(
                file))
        return response.text

    @property
    def log(self):
        response = requests.get(self.base_url + self.port + '/getLog')
        return response.text


class CEditingSession(RestAPI):

    @property
    def guid(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/guid')
        return response.text

    @property
    def agency(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/A'
            'gency')
        return response.text

    @property
    def catalogpreviewimage(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'atalogPreviewImage')
        return response.text

    @property
    def contentcomposite(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'ontentComposite')
        return response.text

    @property
    def contentimage(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'ontentImage')
        return response.text

    @property
    def contenttext(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'ontentText')
        return response.text

    @property
    def project(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/P'
            'roject')
        return response.text

    @property
    def references(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/R'
            'eferences')
        return response.text

    @property
    def surface(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/S'
            'urface')
        return response.text

    @property
    def zincdeeplinks(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/Z'
            'incDeepLinks')
        return response.text

    @property
    def app(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/A'
            'pp')
        return response.text

    @property
    def bevelbutton(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/B'
            'evelButton')
        return response.text

    @property
    def checkbox(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'heckBox')
        return response.text

    @property
    def cmpcontentelement(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'mpContentElement')
        return response.text

    @property
    def disclosuretriangle(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/D'
            'isclosureTriangle')
        return response.text

    @property
    def ceditingsession(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/C'
            'EditingSession')
        return response.text

    @property
    def listbox(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/L'
            'istBox')
        return response.text

    @property
    def popupmenu(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/P'
            'opupMenu')
        return response.text

    @property
    def pushbutton(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/P'
            'ushButton')
        return response.text

    @property
    def textarea(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/T'
            'extArea')
        return response.text

    @property
    def textfield(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/T'
            'extField')
        return response.text

    @property
    def window(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/W'
            'indow')
        return response.text

    @property
    def windowpane(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/W'
            'indowPane')
        return response.text

    @property
    def error(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/E'
            'rror')
        return response.text

    @property
    def nodeguid(self):
        response = requests.get(
            self.base_url + self.port + '/get/CEditingSession/automationType/n'
            'odeguid')
        return response.text


class WndAssemblerPalette(RestAPI):

    @property
    def bntprev(self):
        response = requests.get(
            self.base_url + self.port + '/get/WndAssemblerPalette/BtnPrev')
        return response.text


class WndContentEditor(RestAPI):

    @property
    def status(self):
        response = requests.get(
            self.base_url + self.port + '/get/WndContentEditor/Status')
        return response.text


class WndDummyFocus(RestAPI):
    pass


class WndPreferences(RestAPI):
    pass


if __name__ == '__main__':
    r = RestAPI()
    print 'Table of Contents: {}'.format(r.toc)
    print 'Get test_ingestor script contents: {}'.format(
        r.getFile(
            '%2FUsers%2Fcary%2FProjects%2Fheadway_consulting%2Fmerck%2Fcode%2F'
            'test_ingestor.sh'))
    print 'Logs: {}'.format(r.log)

    c = CEditingSession()
    print 'CEditingSession guid: {}'.format(c.guid)
    print 'CEditingSession Agency: {}'.format(c.agency)
    print 'CEditingSession CatalogPreviewImage: {}'.format(c.catalogpreviewimage)
    print 'CEditingSession ContentComposite: {}'.format(c.contentcomposite)
    print 'CEditingSession ContentImage: {}'.format(c.contentimage)
    print 'CEditingSession ContentText: {}'.format(c.contenttext)
    print 'CEditingSession Project: {}'.format(c.project)
    print 'CEditingSession References: {}'.format(c.references)
    print 'CEditingSession Surface: {}'.format(c.surface)
    print 'CEditingSession ZincDeepLinks: {}'.format(c.zincdeeplinks)
    print 'CEditingSession App: {}'.format(c.app)
    print 'CEditingSession BevelButton: {}'.format(c.bevelbutton)
    print 'CEditingSession CheckBox: {}'.format(c.checkbox)
    print 'CEditingSession CmpContentElement: {}'.format(c.cmpcontentelement)
    print 'CEditingSession DisclosureTriangle: {}'.format(c.disclosuretriangle)
    print 'CEditingSession CEditingSession: {}'.format(c.ceditingsession)
    print 'CEditingSession ListBox: {}'.format(c.listbox)
    print 'CEditingSession PopupMenu: {}'.format(c.popupmenu)
    print 'CEditingSession PushButton: {}'.format(c.pushbutton)
    print 'CEditingSession TextArea: {}'.format(c.textarea)
    print 'CEditingSession TextField: {}'.format(c.textfield)
    print 'CEditingSession Window: {}'.format(c.window)
    print 'CEditingSession WindowPane: {}'.format(c.windowpane)
    print 'CEditingSession Error: {}'.format(c.error)
    print 'CEditingSession nodeguid: {}'.format(c.nodeguid)

    wa = WndAssemblerPalette()
    print 'WndAssemblerPalette BtnPrev: {}'.format(wa.bntprev)

    wc = WndContentEditor()
    print 'WndContentEditor Status: {}'.format(wc.status)
