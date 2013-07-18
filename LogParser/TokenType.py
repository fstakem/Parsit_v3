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
# None

class TokenType(object):
    """This class represents a token type that is found in a scanned file."""
       
    # Class constants
    NONE = 0
    OBJECT = 1
    
    readable_name = {
                     NONE:                'None',
                     OBJECT:              'Object',
                    }
     
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
    
    
    