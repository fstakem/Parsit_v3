# ------------------------------------------------------
#
#   ScannerState.py
#   By: Fred Stakem
#   Created: 3.30.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from LogParser import ScannerState as BaseScannerState

class ScannerState(object):
    """This class represents the state of the scanner."""
       
    # Class constants
    START = 0
    SCANNED_DATETIME = 1
    SCANNED_PID = 2
    SCANNED_TID = 3
    SCANNED_LEVEL = 4
    SCANNED_SOURCE = 5
    SCANNED_MSG = 6
    
    readable_name = {
                     START:                     'Start',
                     SCANNED_DATETIME:          'Scanned Datetime',
                     SCANNED_PID:               'Scanned PID',
                     SCANNED_TID:               'Scanned TID',
                     SCANNED_LEVEL:             'Scanned Level',
                     SCANNED_SOURCE:            'Scanned Source',
                     SCANNED_MSG:               'Scanned Message',
                    }
     
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
    
     
    
    
    
    
    