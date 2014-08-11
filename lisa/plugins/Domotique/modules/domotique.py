# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
# project     : Lisa plugins
# module      : Domotique
# file        : domotique.py
# description : Manage domotic orders with home domotic computer
# author      : G.Audet
#-----------------------------------------------------------------------------
# copyright   : Neotique
#-----------------------------------------------------------------------------

# TODO :


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os, sys



#-----------------------------------------------------------------------------
# Plugin Domotique class
#-----------------------------------------------------------------------------
class Domotique(IPlugin):
    """
    Plugin main class
    """
    def __init__(self):
        super(Domotique, self).__init__(plugin_name = "Domotique")
        
    #-----------------------------------------------------------------------------
    #              Publics  Fonctions
    #-----------------------------------------------------------------------------
    def on_offDomo(self, jsonInput):
        """
        start and stop home equipement via domotic central
        """
        #print jsonInput

        # Get informations
        onoff =  u''  # on or off
        loc = u'all'
        obj = u''  #lights, windows, door....
        try:
            if 'on_off' in jsonInput['outcome']['entities']:
                onoff = (jsonInput['outcome']['entities']['on_off']['value'])
            if 'message_subject' in jsonInput['outcome']['entities']:
                obj = (jsonInput['outcome']['entities']['message_subject']['value'])
            if 'location' in jsonInput['outcome']['entities']:
                loc = (jsonInput['outcome']['entities']['location']['value'])      
        except UnicodeEncodeError:
            return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body':"Erreur d'encodage du texte" }
        except:
            return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body': self._("error") }
        
        if onoff =="" :
            return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body': self._("dont understand") }
        #if loc or obj ==""  -> non   fatal

        if __name__ == "__main__" :
            print '{0:10} {1:10}'.format('on',onoff)
            print '{0:10} {1:10}'.format('loc',loc)
            print '{0:10} {1:10}'.format('obj',obj)

        #action
        #TODO
        if loc == 'all':
            loc = self._('all')
        else :
            loc = self._('inside') + loc
        message = self._('I do').format(on = self._(onoff), obj = obj, loc = loc)
                
        return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body': message }

    #-----------------------------------------------------------------------------
    def setDomo(self, jsonInput):
        """
        set a specific control to a specific equipement
        """
        pass

    #-----------------------------------------------------------------------------
    def getDomo(self, jsonInput):
        """
        Get a status about equipement
        """
         #print jsonInput

        # Get informations
        loc =u'all'
        obj=u''
        try:
            if 'message_subject' in jsonInput['outcome']['entities']:
                obj = (jsonInput['outcome']['entities']['message_subject']['value'])
            if 'location' in jsonInput['outcome']['entities']:
                loc = (jsonInput['outcome']['entities']['location']['value'])
        except UnicodeEncodeError:
            return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body':"Erreur d'encodage du texte" }
        except:
            return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body': self._("error") }
            

        if __name__ == "__main__" :
            print '{0:10} {1:10}'.format('loc',loc)
            print '{0:10} {1:10}'.format('obj',obj)

        #action
        #TODO
        if loc == 'all':
            loc = self._('all')
        else :
            loc = self._('inside') + loc
        message = self._('status').format(obj = obj, loc = loc, stat = self._('rnd'))
        return {"plugin": __name__.split('.')[-1], "method": sys._getframe().f_code.co_name, 'body': message }


#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------
if __name__ == "__main__" :
    jsonInput = {'from': u'Lisa-Web', 'zone': u'WebSocket', u'msg_id': u'67765841-b544-4896-89ea-52ab4dfb6001',
    u'msg_body': u'éteins les lumières dans le salon',
    u'outcome': {
        u'entities': {
            u'on_off': {u'value': u'on'},
            u'location': {u'body': u'le salon', u'start': 25, u'end': 33, u'suggested': True, u'value': u'le salon'},
            u'message_subject': {u'body': u'lumières', u'start': 11, u'end': 19, u'suggested': True, u'value': u'les lumières'}
            },
        u'confidence': 0.999,
        u'intent': u'domo_get'
        },
    'type': u'chat'}

    essai = Domotique() #class init

    ret = essai.on_offDomo(jsonInput)
    #ret = essai.getDomo(jsonInput)
    print ret['body']

# --------------------- End of domotique.py  ---------------------
