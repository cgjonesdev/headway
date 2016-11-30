#!/usr/bin/env python

'''
Provides an interface to the Assembler application's TCP socket.
'''

import sys
import os
import time
from datetime import datetime
from hashlib import md5
import requests
from urllib import quote_plus, unquote_plus
from meta import RequestMeta
from config import AssemblerConfig
from logger import logger

cfg                     = AssemblerConfig('{}/configs/assembler.cfg'.format(
                                          os.environ['ASSEMBLER_TESTS']))

SCHEME                  = cfg['SCHEME']
HOST                    = sys.argv[1] if len(sys.argv) > 1 else cfg['HOST']
PORT                    = ':{}'.format(sys.argv[2] if len(sys.argv) > 2 else \
                          cfg['PORT'])

RETURN_OK               = 'OK'
RETURN_ERROR            = 'ERROR'
RETURN_UNDEFINED        = 'UNDEFINED'

FILE_RETURN_DIRECTORY   = 'DIRECTORY'
FILE_RETURN_FILE        = 'FILE'
FILE_RETURN_NOT_EXISTS  = 'NOT_EXISTS'
FILE_LOC_DESKTOP        = 'desktop'
FILE_LOC_HOME           = 'home'
FILE_LOC_TMP            = 'tmp'

WINDOW_PREFERENCES      = 'WndPreferences%2F'
SET_ROLE                = WINDOW_PREFERENCES + 'PupRole/value'
SET_CHK_DEBUG_MODE      = WINDOW_PREFERENCES + 'ChkDebugMode/value'
CLICK_OK                = WINDOW_PREFERENCES + 'BtnOK'
CLICK_CANCEL            = WINDOW_PREFERENCES + 'BtnCancel'

class Base(object):
    '''
    Purpose: Serves as the base class for Requests so that common attributes
    can be inherited instead of being duplicated.
    '''

    def __str__(self):
        '''
        Purpose: Sets the class's string representation of itsself to a simpler,
        more intuitive output that the standard implementation of
        <__main__.Base object at 0x10614e310>
        '''
        return self.__class__.__name__

class Lock(object):
    '''
    Purpose: To provide an interface to the application lock.

    Function: Expose an "open" property that unlocks the application when
    accessed as a getter for the object.
    '''
    locked = True
    today_utc = datetime.utcnow()
    key_str = 'TheSecretNumberIs{}{}{}{}{}'.format(
        str(today_utc.year % 59),
        str(today_utc.month + 17),
        str(today_utc.day + 20),
        str(today_utc.hour + 37),
        str(today_utc.minute + 17))
    m = md5()
    m.update(key_str)
    digest = m.hexdigest()

    def __init__(self, url):
        '''
        Sets the url for the lock. This has to be here because the base_url is
        set in the Request class because that's where it gets used the most.
        '''
        self.url = url

    def __nonzero__(self):
        '''
        Purpose: Checks if the lock is applied.

        Returns: Boolean True if locked, False if not.
        '''
        return self.locked

    @property
    def open(self):
        '''
        Opens the lock which makes the listener available for requests.
        '''
        logger.info('Opening the lock on host {}{}...'.format(HOST, PORT))
        response = requests.get(
            self.url + 'knockKnockItsMe/{}'.format(self.digest))
        if response.text == RETURN_OK:
            self.locked = False

class Request(Base):
    '''
    Purpose: To provide objects that can access the Assembler application via
    OOP concepts.

    Function: Perform API calls to specific endpoints via the class's resource
    attribute
    '''
    __metaclass__ = RequestMeta
    base_url = SCHEME + HOST + PORT + '/'
    lock = Lock(base_url)

    def __init__(self):
        '''
        When an object is created the contructor check for the lock condition.
        If applied, the lock is removed and the applicaiton is opened for use.
        '''
        self.unlock

    @property
    def unlock(self):
        ''' Unlocks the application for use '''
        if self.lock.locked:
            self.lock.open

    def __repr__(self):
        '''
        Purpose: Render a representation of what the object is retrieving via
        an API call. This is intuitive because __repr__ can be used to present
        the object any way that displays it's internals. Wrapping an object in
        repr() provides a simple way to make a call against the applicaiton's
        programming interface.

        Function: Perform an API call using Python's request module.

        Usage: repr(obj)

        Returns: The response text from the application.
        '''
        resource = self.resource if hasattr(self, 'resource') else ''
        url = self.base_url + resource
        logger.info('Sending request to: ' + url)
        text = requests.get(url).text.encode('utf-8')
        logger.info(
            'Response from {}: {}'.format(
                self.base_url[:-1], unquote_plus(text)))
        # if ('quit' not in self.resource and not (RETURN_ERROR in self.resource
        #     or isinstance(self, (Logs.Message, Logs.Get)))):
        #     assert RETURN_ERROR not in text, text
        return text

    def __getitem__(self, key):
        '''
        Purpose: Prepend get/ to a resource. This is intuitive because it is
        performing a get type of functionality.

        Function: Perform an API call using Python's request module where get/
        is inserted between the root "/" and the resource being requested.

        Usage: obj['resource']

        Returns: The response text from the application.
        '''
        self.resource = 'get/' + key
        return repr(self)

    def __setitem__(self, key, value):
        '''
        Purpose: Prepend set/ to a resource. This is intuitive because it is
        performing a set type of functionality.

        Function: Perform an API call using Python's request module where set/
        is inserted between the root "/" and the resource being requested.

        Usage: obj['resource'] = value

        Returns: The response text from the application.
        '''
        self.resource = 'set/{}/{}'.format(key, value)
        return repr(self)

    def __call__(self, action, *resources):
        '''
        Purpose: Prepend <action>/ to a resource. This is intuitive because it
        facilitates a callback-like action such as an event handler would make
        available.

        Function: Perform an API call using Python's request module where
        <action>/ is inserted between the root "/" and <resource>, which is the
        resource being requested.

        Usage: obj(action, resource)

        Returns: The response text from the application.
        '''
        self.resource = action + '/'.join(*resources)
        return repr(self)

class Remote(Request):

    def __init__(self, parent, target):
        Request.__init__(self)
        self.parent, self.target = parent, target

class Selector(Request):

    def __init__(self, obj, query):
        Request.__init__(self)

class Window(Request):
    
    class Preferences(Request):
        pass

    class AttributeValue(Request):
        pass

    class ContentEditor(Request):
        pass

class UI(Request):
    pass

class Object(Request):

    def __getitem__(self, handle=None):
        self.resource = '{}/{}'.format(self.resource, handle)
        return repr(self)

    def __setitem__(self, key, value):
        return NotImplementedError(
            'Cannot call "/set" on a {} object'.format(str(self)))

class Version(Request):
    resource = 'getVersion'

class Toc(Request):
    resource = 'toc'

    class NonRecursive(Request):
        resource = 'toc/0'

    class Recursive(Request):
        resource = 'toc/1'        

class Key(Request):

    class Hold(Request):

        class CtrlOpt(Request):
            resource = 'holdKey/ctrl/opt'

    class Release(Request):
        resource = 'holdKey'

class Menu(Request):
    pass

    class Preferences(Request):
        resource = 'menu/kMenu_MnuPreferences'

    class OpenProject(Object):
        resource = 'menu/kMenu_FileOpen'

class Click(Request):
    resource = 'click'

    class Double(Request):
        resource = 'doubleClick'

class Roles(Request):

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        repr(Key.Hold.CtrlOpt())
        repr(Menu.Preferences())
        self[ROLE_SET] = value
        result = self('click', CLICK_OK)
        logger.info(result)
        repr(Key.Release())

class Drop(Object):
    resource = 'drop'

class File(object):

    class Get(Object):
        resource = 'getFile'

        class Url(Object):
            resource = 'getFileUrl'

    class Exists(Object):
        resource = 'fileExists'

class Logs(object):

    class Get(Object):
        resource = 'getLog'

    class Message(Object):
        resource = 'logMessage'

        @property
        def error(self):
            return self._error

        @error.setter
        def error(self, value):
            self._error = value
            self[value]

        @property
        def warning(self):
            return _error

        @warning.setter
        def warning(self, value):
            self.warning = value
            self[value]

        @property
        def trace(self):
            return self._trace

        @trace.setter
        def trace(self, value):
            self._trace = value
            self[value]

        @property
        def note(self):
            return self._note

        @note.setter
        def note(self, value):
            self._note = value
            self[value]

        class Singleton(Object):
            pass

    class GetLevel(Object):
        resource = 'getLogLevel'

    class Clear(Request):
        resource = 'clearLog'

class Restart(Request):
    resource = 'restart'

class CloseAll(Request):
    resource = 'closeAll'

class Quit(Request):
    resource = 'quit'

if __name__ == '__main__':
    repr(Version())
