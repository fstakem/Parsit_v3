# ------------------------------------------------------
#
#   Token.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
import logging

# User defined
from Utilities import *
from TokenType import TokenType

class Token(object):
    """This class represents a token that is found in a scanned line."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::Token')
    
    def __init__(self, type=TokenType.NONE, data=None, start_position=-1, end_position=-1):
        self.type = type
        self.data = data
        self.start_position = start_position
        self.end_position = end_position
      
    def __str__(self):
        return 'Type: %s Data: %s Position: %s to %s' % (TokenType.prettyPrint(self.type), 
                                                         self.data, 
                                                         str(self.start_position),
                                                         str(self.end_position))
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if other != None and self.type == other.type and self.data == other.data:
            return True
        
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    
    
    
    
    