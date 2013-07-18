# ------------------------------------------------------
#
#   EventType.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libs
import logging

# User defined
from Utilities import *

class EventType(object):
    """This class represents an event type that occurs in a log."""
       
    # Setup logging
    logger = Utilities.getLogger('EventType')
    
    # Class constants
    NONE = 0
    GENERIC = 1
    STATE_TRANSITION = 2
    STATE_ENTER = 3
    STATE_EXIT = 4
    
    readable_name = {
                     NONE:                'None',
                     GENERIC:             'Generic',
                     STATE_TRANSITION:    'State Transition',
                     STATE_ENTER:         'State Enter',
                     STATE_EXIT:          'State Exit'
                    }
    
    @classmethod
    def prettyPrint(cls, event_type):
        return cls.readable_name[event_type]
    
    
    
    