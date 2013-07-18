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
    """This class represents a iOS token type that is found in a scanned file."""
       
    # Class constants
    NONE = 0
    TIMESTAMP = 1
    SOURCE = 2
    PID = 3
    MACH_PORT = 4
    MSG = 5
    
    readable_name = {
                     NONE:         'None',
                     TIMESTAMP:    'Timestamp',
                     SOURCE:       'Source',
                     PID:          'Pid',
                     MACH_PORT:    'Mach Port',
                     MSG:          'Msg',
                    }
    
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
   
    
    
    
    