# ------------------------------------------------------
#
#   TestScanner.py
#   By: Fred Stakem
#   Created: 3.30.13
#
# ------------------------------------------------------


# Libs
import unittest

# User defined
from Globals import *
from Utilities import *
from LogParser import LogSource
from IosLogParser import TokenType
from IosLogParser import Token
from IosLogParser import Scanner
from IosLogParser import ScannerState

class ScannerTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('ScannerTest')
    data_file = '../data/iphone_log_1.txt'
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.source = LogSource('iOS Test Source', None)
        self.scanner = Scanner('iOS Test Scanner', self.source)
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testScannerTimestamp(self):
        timestamp_str = '2013-03-22 22:17:52.317'
        input_symbols = timestamp_str + ' MobileCalculator'
        expected_token = Token(TokenType.TIMESTAMP, timestamp_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        ScannerTest.logger.debug('Input data: %s' % (input_symbols))
        
        # Timestamp
        self.getNextTokenAndTestEquality(expected_token, 'Timestamp')
        ScannerTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testScannerSource(self):
        source_str = 'MobileCalculator'
        input_symbols = source_str + '[22262:c07]'
        expected_token = Token(TokenType.SOURCE, source_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        self.scanner.state = ScannerState.SCANNED_DATETIME
        ScannerTest.logger.debug('Input data: %s' % (input_symbols))
        
        # Source
        self.getNextTokenAndTestEquality(expected_token, 'Source')
        ScannerTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testScannerPid(self):
        pid_str = '22262'
        input_symbols = 'MobileCalculator[' + pid_str + ':c07]'
        expected_token = Token(TokenType.PID, pid_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        self.scanner.state = ScannerState.SCANNED_DATETIME
        ScannerTest.logger.debug('Input data: %s' % (input_symbols))
        
        # Source
        self.getNextToken()
        
        # PID
        self.getNextTokenAndTestEquality(expected_token, 'PID')
        ScannerTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testScannerMachPort(self):
        mach_port_str = 'c07'
        input_symbols = 'MobileCalculator[22262:' + mach_port_str + ']'
        expected_token = Token(TokenType.MACH_PORT, mach_port_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        self.scanner.state = ScannerState.SCANNED_DATETIME
        ScannerTest.logger.debug('Input data: %s' % (input_symbols))
        
        # Source
        self.getNextToken()
        
        # PID
        self.getNextToken()
        
        # Mach port
        self.getNextTokenAndTestEquality(expected_token, 'Mach port')
        ScannerTest.logger.debug('Test succeeded!')
        
    @log_test(logger, globals.log_separator)
    def testScannerMsg(self):
        msg_str = 'Digit pressed: 8'
        input_symbols = msg_str + '\n'
        expected_token = Token(TokenType.MSG, msg_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        self.scanner.state = ScannerState.SCANNED_MACH_PORT
        ScannerTest.logger.debug('Input data: %s' % (input_symbols[:-1]))
        
        # Msg
        self.getNextTokenAndTestEquality(expected_token, 'Message')
        ScannerTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testScannerLine(self):
        timestamp_str = '2013-03-22 22:17:52.317'
        source_str = 'MobileCalculator'
        pid_str = '22262'
        mach_port_str = 'c07'
        msg_str = 'Digit pressed: 8'
        input_symbols = '%s %s[%s:%s] %s\n' % (timestamp_str, source_str, pid_str, mach_port_str, msg_str)
        
        # Expected tokens
        timestamp_token = Token(TokenType.TIMESTAMP, timestamp_str)
        source_token = Token(TokenType.SOURCE, source_str)
        pid_token = Token(TokenType.PID, pid_str)
        mach_port_token = Token(TokenType.MACH_PORT, mach_port_str)
        msg_token = Token(TokenType.MSG, msg_str)
        
        # Setup
        self.scanner.reset(input_symbols)
        ScannerTest.logger.debug('Input data: %s' % (input_symbols[:-1]))
        
        # Timestamp
        self.getNextTokenAndTestEquality(timestamp_token, 'Timestamp')
        
        # Source
        self.getNextTokenAndTestEquality(source_token, 'Source')
        
        # PID
        self.getNextTokenAndTestEquality(pid_token, 'PID')
        
        # Mach port
        self.getNextTokenAndTestEquality(mach_port_token, 'Mach port')
        
        # Msg
        self.getNextTokenAndTestEquality(msg_token, 'Message')
        ScannerTest.logger.debug('Test succeeded!')
        
    @log_test(logger, globals.log_separator)
    def testScannerRealData(self):
        ScannerTest.logger.debug('Testing data in the file: ' + ScannerTest.data_file)
        lines = readLinesFromFile(ScannerTest.data_file)
        
        for line in lines:
            line += '\n'
            
        errors = []
            
        for i, line in enumerate(lines):
            token = 1
            self.scanner.reset(line)
            ScannerTest.logger.debug('Scanning line %d' % (i+1))
            ScannerTest.logger.debug('Input data: %s' % (line[:-1]))
            while token != None:
                token, error = self.getNextToken()
                
                if error != None:
                    errors.append(error)
                                    
        if len(errors) != 0:
            ScannerTest.logger.debug('Found the following errors scanning the file:')
            for i, error in enumerate(errors):
                start_position = error[0] 
                current_position = error[1] 
                error_except = error[2]
                output = 'Error: %s Start position: %d End position: %d' % (str(error_except), start_position, current_position)
                ScannerTest.logger.debug(output)
                
            assert False, 'Found %d errors scanning the file.' % (str(len(errors) + 1))
                
        ScannerTest.logger.debug('Test succeeded!')
        
    def getNextTokenAndTestEquality(self, expected_token, type_str):
        ScannerTest.logger.debug('Expected token: %s' % (str(expected_token)))
        token, error = self.getNextToken()
        output = '%s string was incorrectly scanned.' % (type_str)
        assert token == expected_token, output
        
        return token
        
    def getNextToken(self):
        token, current_symbol, state, error = self.scanner.scan()   
        assert error == None, error[2]
        ScannerTest.logger.debug('Scanned token: %s' % (str(token)))
        
        return (token, error)
    
        
   
   
   
