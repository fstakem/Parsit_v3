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
# None

class ScannerState(object):
    """This class represents the state of the scanner."""
       
    # Class constants
    START = 0
    END = 1
    
    readable_name = {
                     START:            'Start',
                     END:              'End',
                    }
     
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
    
    
    