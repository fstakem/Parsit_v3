# ------------------------------------------------------
#
#   Parser.py
#   By: Fred Stakem
#   Created: 3.5.13
#
# ------------------------------------------------------


# Libs
from datetime import datetime
import Utilities

# User defined
from LogParser import Parser as BaseParser
from LogParser import Symbol
from LogParser import ScanException
from LogParser import ParseException
from LogLine import LogLine
from Log import Log
from Scanner import ScannerState
from TokenType import TokenType
from LogLine import LogLevel

class Parser(BaseParser):
    
    # Setup logging
    logger = Utilities.getLogger('AndroidLogParser::Parser')
    
    def __init__(self, name, scanner):
        super(Parser, self).__init__(name, scanner)
        self.__import__()
        
    def parse(self, name, log_lines):
        parsed_lines = []
        errors = []
        for i, line in enumerate(log_lines):
            try:
                parsed_lines.append( self.parseLogLine(line) )
            except ParseException, e:
                errors.append( (i, e.msg()) )
            
        log = Log()
        log.name = name
        log.lines = parsed_lines
        
        return (log, errors) 
    
    def parseLogLine(self, line):
        log_line = LogLine(line)
        self.scanner.reset(line)
        
        while True:
            token, current_symbol, state, error = self.scanner.scan()
        
            if token == None and error != None:
                raise ScanException(str(error[3]))
            elif token == None and Symbol.isEol(current_symbol) and state == ScannerState.SCANNED_MSG:
                return log_line
            elif token.type == TokenType.TIMESTAMP:
                log_line.timestamp = self.parseDateTime(token)
            elif token.type == TokenType.PID:
                log_line.pid = self.parsePid(token)
            elif token.type == TokenType.TID:
                log_line.tid = self.parseTid(token)
            elif token.type == TokenType.LEVEL:
                log_line.level = self.parseLevel(token)
            elif token.type == TokenType.SOURCE:
                log_line.source = self.parseSource(token)
            elif token.type == TokenType.MSG:
                log_line.msg = self.parseMsg(token)
            else:
                raise ParseException('Unknown token returned by the scanner.')
        
        raise ParseException('End of line not found.')
    
    def parseDateTime(self, token):
        dt = datetime.now()
        subtokens = token.data.split()
        
        date_subtokens = subtokens[0].split('-')
        if len(date_subtokens) < 2:
            raise ParseException('Error parsing date subtoken: %s' % (date_subtokens))
        month = int(date_subtokens[0])
        day = int(date_subtokens[1])
        
        time_subtokens = subtokens[1].split(':')
        if len(time_subtokens) < 3:
            raise ParseException('Error parsing time subtoken: %s' % (time_subtokens))
        hour = int(time_subtokens[0])
        minute = int(time_subtokens[1])
        
        seconds_subtokens = time_subtokens[2].split('.')
        if len(seconds_subtokens) < 2:
            raise ParseException('Error parsing seconds subtoken: %s' % (seconds_subtokens))
        second = int(seconds_subtokens[0])
        microsecond = int(seconds_subtokens[1]) * 1000
        
        new_dt = datetime(dt.year, month, day, hour, minute, second, microsecond)
 
        return new_dt
    
    def parsePid(self, token):
        try:
            pid = int(token.data)
            return pid
        except ValueError:
            raise ParseException('Error parsing pid token: %s' % str(token))
            
    def parseTid(self, token):
        try:
            tid = int(token.data)
            return tid
        except ValueError:
            raise ParseException('Error parsing tid token: %s' % str(token))
    
    def parseLevel(self, token):
        if token.data == 'V':
            return LogLevel.Verbose
        elif token.data == 'I':
            return LogLevel.Info
        elif token.data == 'D':
            return LogLevel.Debug
        elif token.data == 'W':
            return LogLevel.Warn
        elif token.data == 'E':
            return LogLevel.Error
        elif token.data == 'A':
            return LogLevel.Assert
        else:
            raise ParseException('Error parsing level token: %s' % str(token))
    
    def parseSource(self, token):
        return token.data
    
    def parseMsg(self, token):
        return token.data
    
    
    
    