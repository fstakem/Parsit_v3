# ------------------------------------------------------
#
#   Scanner.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------


# Libs
from Globals import *
from Utilities import *

# User defined
from LogParser import Symbol
from LogParser import Scanner as BaseScanner
from LogParser import ScanException
from TokenType import TokenType
from Token import Token
from ScannerState import ScannerState

class Scanner(BaseScanner):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidLogParser::Scanner')
    
    def __init__(self, name, source):
        super(Scanner, self).__init__(name, source)
        self.state = ScannerState.START
     
    def reset(self, symbols=''):
        self.state = ScannerState.START
        super(Scanner, self).reset(symbols)

    @debug_log(logger, globals.debug_scan)
    def scan(self):
        while True:
            self.getNextSymbol()
            self.start_position = self.current_position
            Scanner.logger.debug('Initial symbol: %s' % (self.current_symbol))
            
            if Symbol.isEol(self.current_symbol):
                return (None, self.current_symbol, self.state, None)
            elif Symbol.isSeparator(self.current_symbol):
                continue
            else:
                try:
                    token = self.scanToken()
                    return (token, self.current_symbol, self.state, None)
                except Exception as e:
                    error = (self.start_position, self.current_position, e)
                    return (None, self.current_symbol, self.state, error)
            
    def __str__(self):
        output = super(Scanner, self).__str__()
        output += 'Scanner state: %s' % (ScannerState.prettyPrint(self.state))
        
        return output
                     
    def scanToken(self):
        self.symbol_buffer = ''
        
        if self.state == ScannerState.START:
            return self.scanDateTime()
        elif self.state == ScannerState.SCANNED_DATETIME:
            return self.scanPid()
        elif self.state == ScannerState.SCANNED_PID:
            return self.scanTid()
        elif self.state == ScannerState.SCANNED_TID:
            return self.scanLevel()
        elif self.state == ScannerState.SCANNED_LEVEL:
            return self.scanSource()
        elif self.state == ScannerState.SCANNED_SOURCE:
            return self.scanMsg()
        
        return None
            
    def scanDateTime(self):
        while Symbol.isDigit(self.current_symbol) or \
              Symbol.isDash(self.current_symbol):
            self.acceptSymbol()
            
        while Symbol.isSeparator(self.current_symbol):
            self.acceptSymbol()
            
        while Symbol.isDigit(self.current_symbol) or \
              Symbol.isColon(self.current_symbol) or \
              Symbol.isDot(self.current_symbol):
            self.acceptSymbol()
            
        tokens = self.symbol_buffer.split()
        if len(tokens) < 2:
            raise ScanException('Date time has incorrect number of subtokens.')
        elif len(tokens[0]) < 5:
            raise ScanException('First date time subtoken is incorrect length.')
        elif len(tokens[1]) < 12:
            raise ScanException('Second date time subtoken is incorrect length.')
        
        self.state = ScannerState.SCANNED_DATETIME
        
        return Token(TokenType.TIMESTAMP, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanPid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol()
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No PID symbols found.')
        
        self.state = ScannerState.SCANNED_PID
        
        return Token(TokenType.PID, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanTid(self):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol()
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No TID symbols found.')
        
        self.state = ScannerState.SCANNED_TID
        
        return Token(TokenType.TID, self.symbol_buffer, self.start_position, self.current_position-1)
    
    def scanLevel(self):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol()
            
        if len(self.symbol_buffer) != 1:
            raise ScanException('Incorrect number of symbols for the log level.')
        
        self.state = ScannerState.SCANNED_LEVEL
        
        return Token(TokenType.LEVEL, self.symbol_buffer, self.start_position, self.current_position-1)

    def scanSource(self):
        # TODO
        # This needs to made more robust because more
        # symbols are definately possible even though
        # they are not often used.
        # One known error is there is no source.
        while Symbol.isCharacter(self.current_symbol) or \
              Symbol.isDigit(self.current_symbol) or \
              Symbol.isUnderscore(self.current_symbol) or \
              Symbol.isSeparator(self.current_symbol) or \
              Symbol.isForwardSlash(self.current_symbol):
            self.acceptSymbol()
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No source symbols found.') 
        
        self.state = ScannerState.SCANNED_SOURCE
        
        return Token(TokenType.SOURCE, self.symbol_buffer.strip(), self.start_position, self.current_position-2)

    def scanMsg(self):
        while not Symbol.isEol(self.current_symbol):
            self.acceptSymbol()
            
        if len(self.symbol_buffer) < 1:
            raise ScanException('No msg symbols found.') 
        
        self.state = ScannerState.SCANNED_MSG
        
        return Token(TokenType.MSG, self.symbol_buffer, self.start_position, self.current_position-1)

    
    
    
    
    
    
    
    