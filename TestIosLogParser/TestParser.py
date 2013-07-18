# ------------------------------------------------------
#
#   TestParser.py
#   By: Fred Stakem
#   Created: 3.23.13
#
# ------------------------------------------------------


# Libs
import unittest
from datetime import datetime

# User defined
from Globals import *
from Utilities import *
from LogParser import LogSource
from IosLogParser import LogLine
from IosLogParser import Scanner
from IosLogParser import Parser
from IosLogParser import Token
from IosLogParser import TokenType

class ParserTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('ParserTest')
    data_file = '../data/iphone_log_1.txt'
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        source = LogSource('iOS Test Source', None)
        scanner = Scanner('iOS Test Scanner', source)
        self.parser = Parser('iOS Test Parser', scanner)
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testParseTimestamp(self):
        token_data = '2013-03-22 22:17:52.317'
        year = 2013
        month = 03
        day = 22
        hour = 22
        minute = 17
        second = 52
        microsecond = 317000
        expected_output = datetime(year, month, day, hour, minute, second, microsecond)
        self.parseToken(TokenType.TIMESTAMP, token_data, expected_output)
            
        ParserTest.logger.debug('Test succeeded!')
        
    @log_test(logger, globals.log_separator)
    def testParseSource(self):
        token_data = 'MobileCalculator'
        expected_output = token_data
        self.parseToken(TokenType.SOURCE, token_data, expected_output)
        
        ParserTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testParsePid(self):
        token_data = '22262'
        expected_output = int(token_data)
        self.parseToken(TokenType.PID, token_data, expected_output)
        
        ParserTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testParseMachPort(self):
        token_data = 'c07'
        expected_output = token_data
        self.parseToken(TokenType.MACH_PORT, token_data, expected_output)
            
        ParserTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testParseMsg(self):
        token_data = 'Digit pressed: 8'
        expected_output = token_data
        self.parseToken(TokenType.MSG, token_data, expected_output)
            
        ParserTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testParseLine(self):
        timestamp_str = '2013-03-22 22:17:52.317'
        source_str = 'MobileCalculator'
        pid_str = '22262'
        mach_port_str = 'c07'
        msg_str = 'Digit pressed: 8'
        input_symbols = '%s %s[%s:%s] %s\n' % (timestamp_str, source_str, pid_str, mach_port_str, msg_str)
        
        # Expected output
        expected_timestamp = datetime(2013, 03, 22, 22, 17, 52, 317000)
        expected_source = source_str
        expected_pid = int(pid_str)
        expected_mach_port = mach_port_str
        expected_msg = msg_str
        
        # Setup
        ParserTest.logger.debug('Input data: %s' % (input_symbols[:-1]))
        
        # Log line
        try:
            log_line = self.parser.parseLogLine(input_symbols)
            
            assert log_line.timestamp == expected_timestamp, 'Error parsing the timestamp: %s' % (str(log_line.timestamp))
            ParserTest.logger.debug('Parsed the timestamp properly.')
            assert log_line.source == expected_source, 'Error parsing the source: %s' % (log_line.source)
            ParserTest.logger.debug('Parsed the source properly.')
            assert log_line.pid == expected_pid, 'Error parsing the PID: %s' % (str(log_line.pid))
            ParserTest.logger.debug('Parsed the PID properly.')
            assert log_line.mach_port == expected_mach_port, 'Error parsing the mach port: %s' % (str(log_line.mach_port))
            ParserTest.logger.debug('Parsed the mach port properly.')
            assert log_line.msg == expected_msg, 'Error parsing the msg: %s' % (log_line.msg)
            ParserTest.logger.debug('Parsed the msg properly.')
        except Exception as e:
            assert False, 'Error parsing line : %s' % (str(e))
            
        ParserTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testParseRealData(self):
        ParserTest.logger.debug('Testing data in the file: ' + ParserTest.data_file)
        lines = readLinesFromFile(ParserTest.data_file)
        
        for line in lines:
            line += '\n'
            
        log, errors = self.parser.parse('Test iOS Log', lines)
                                        
        if len(errors) != 0:
            ParserTest.logger.debug('Found the following errors parsing the file:')
            for i, error in enumerate(errors):
                error_except = error[2]
                output = 'Error: %s' % (str(error_except))
                ParserTest.logger.debug(output)
                
            assert False, 'Found %d errors parsing the file.' % (str(len(errors) + 1))
                
        ParserTest.logger.debug('Test succeeded!')
      
    def parseToken(self, token_type, input_str, expected_output):
        token = Token(token_type, input_str)
        token_type_str = TokenType.readable_name[token_type]
        
        # Setup
        ParserTest.logger.debug('Input data: %s' % (input_str))
        
        # Message
        output = None
        try:
            ParserTest.logger.debug('Expected %s: %s' % (token_type_str, expected_output))
            if token_type == TokenType.TIMESTAMP:
                output = self.parser.parseDateTime(token)
            elif token_type == TokenType.SOURCE:
                output = self.parser.parseSource(token)
            elif token_type == TokenType.PID:
                output = self.parser.parsePid(token)
            elif token_type == TokenType.MACH_PORT:
                output = self.parser.parseMachPort(token)
            elif token_type == TokenType.MSG:
                output = self.parser.parseMsg(token)
            
            ParserTest.logger.debug('Parsed %s: %s' % (token_type_str, str(output)))
            assert output == expected_output, token_type_str + ' token incorrectly parsed.'
        except Exception as e:
            assert False, 'Error parsing %s: %s' % (token_type_str, str(e))
            
        return output
    
    
    
        
   
