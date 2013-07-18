# ------------------------------------------------------
#
#   LogSource.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Utilities import *
from Symbol import Symbol

class LogSource(object):
    """This class represents a log source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::LogSource')
    
    def __init__(self, name='Generic Source', symbols=''):
        self.name = name
        self.setSymbols(symbols)
        
    def setSymbols(self, symbols=''):
        self.symbols = symbols
        self.previous_symbol = ''
        self.current_position = -1
    
    def getNextSymbol(self):
        self.current_position += 1
        
        try:
            next_symbol = self.symbols[self.current_position]
            self.previous_symbol = next_symbol
            
            return (next_symbol, self.current_position)
        except IndexError:
            self.current_position -= 1
            return (Symbol.EOL[0], self.current_position)
        except Exception:
            self.current_position -= 1
            return (Symbol.UNKNOWN, self.current_position)
        
        
    
            