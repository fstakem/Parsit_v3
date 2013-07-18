# ------------------------------------------------------
#
#   Scanner.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
import logging

# User defined
from Globals import *
from Utilities import *
from Symbol import Symbol

class Scanner(object):
    """This class represents a scanner that scans a log line outputting tokens."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::Scanner')
    
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.reset()
        
    def reset(self, symbols=''):
        self.current_symbol = ''
        self.previous_symbol = ''
        self.start_position = -1
        self.current_position = -1
        self.symbol_buffer = ''
        self.source.setSymbols(symbols)
        
    def scan(self):
        pass
    
    @debug_log(logger, globals.debug_next_symbol)
    def getNextSymbol(self):
        self.previous_symbol = self.source.previous_symbol
        self.current_symbol, self.current_position = self.source.getNextSymbol()
    
    def acceptSymbol(self):
        self.symbol_buffer += self.current_symbol
        self.getNextSymbol()
        
    def __str__(self):
        output = 'Scanner: %s\n' % (self.name)
        output += 'Source: %s\n' % (self.source.name)
        output += 'Current symbol: %s\n' % (self.current_symbol)
        output += 'Previous symbol: %s\n' % (self.previous_symbol)
        output += 'Start position: %d\n' % (self.start_position)
        output += 'Current position: %d\n' % (self.current_position)
        output += 'Symbol buffer: %s\n' % (self.symbol_buffer)
        
        return output
        
    
    
    
    
    
    
    
    
    
            
 