# ------------------------------------------------------
#
#   Parser.py
#   By: Fred Stakem
#   Created: 3.23.13
#
# ------------------------------------------------------


# Libs
from datetime import datetime

# User defined
from Globals import *
from Utilities import *
from LogParser import Symbol
from LogParser import Parser as BaseParser
from LogParser import ScanException
from LogParser import ParseException
from LogLine import LogLine
from Log import Log
from ScannerState import ScannerState
from TokenType import TokenType

class Parser(BaseParser):
    
    # Setup logging
    logger = Utilities.getLogger('IosLogParser::Parser')
    
    def __init__(self, name, scanner):
        super(Parser, self).__init__(name, scanner)
        
    def parse(self, name, log_lines):
        self.parsed_lines = []
        self.errors = []
        for i, line in enumerate(log_lines):
            try:
                self.parsed_lines.append( self.parseLogLine(line) )
            except ScanException, e:
                self.errors.append( (i, str(e)) )
            except ParseException, e:
                self.errors.append( (i, str(e)) )
            
        log = Log()
        log.name = name
        log.lines = self.parsed_lines
        
        return (log, self.errors) 
    
    def __str__(self):
        output = super(Parser, self).__str__()
        
        return output
    
    @debug_log(logger, globals.debug_parse)
    def parseLogLine(self, line):
        log_line = LogLine(line)
        self.scanner.reset(line)
        
        while True:
            token, current_symbol, state, error = self.scanner.scan()
            
            if token == None and error != None:
                raise ScanException(str(error[3]))
            if token == None and Symbol.isEol(current_symbol) and state == ScannerState.SCANNED_MSG:
                return log_line
            elif token.type == TokenType.TIMESTAMP:
                log_line.timestamp = self.parseDateTime(token)
            elif token.type == TokenType.SOURCE:
                log_line.source = self.parseSource(token)
            elif token.type == TokenType.PID:
                log_line.pid = self.parsePid(token)
            elif token.type == TokenType.MACH_PORT:
                log_line.mach_port= self.parseMachPort(token)
            elif token.type == TokenType.MSG:
                log_line.msg = self.parseMsg(token)
            else:
                raise ParseException('Unknown token returned by the scanner.')
                    
        
        raise ParseException('End of line not found.')
    
    def parseDateTime(self, token):
        subtokens = token.data.split()
        
        date_subtokens = subtokens[0].split('-')
        if len(date_subtokens) < 2:
            raise ParseException('Error parsing date subtoken: %s' % (date_subtokens))
        year = int(date_subtokens[0])
        month = int(date_subtokens[1])
        day = int(date_subtokens[2])
        
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
        
        dt = datetime(year, month, day, hour, minute, second, microsecond)
        
        return dt
    
    def parseSource(self, token):
        return token.data
    
    def parsePid(self, token):
        try:
            pid = int(token.data)
            return pid
        except ValueError:
            raise ParseException('Error parsing pid token: %s' % str(token))
    
    def parseMachPort(self, token):
        return token.data

    def parseMsg(self, token):
        return token.data
    
    
    
    