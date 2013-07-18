# ------------------------------------------------------
#
#   TokenType.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from LogParser import TokenType as BaseTokenType

class TokenType(BaseTokenType):
    """This class represents a android token type that is found in a scanned file."""
       
    # Class constants
    NONE = 0
    TIMESTAMP = 1
    PID = 2
    TID = 3
    LEVEL = 4
    SOURCE = 5
    MSG = 6
    
    readable_name = {
                     NONE:         'None',
                     TIMESTAMP:    'Timestamp',
                     PID:          'Pid',
                     TID:          'Tid',
                     LEVEL:        'Level',
                     SOURCE:       'Source',
                     MSG:          'Msg',
                    }
    
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
    
    
    