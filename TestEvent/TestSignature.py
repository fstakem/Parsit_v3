# ------------------------------------------------------
#
#   TestSignature.py
#   By: Fred Stakem
#   Created: 4.27.13
#
# ------------------------------------------------------


# Libs
import unittest
from datetime import datetime

# User defined
from Utilities import *
from Globals import *
from SystemEvent import MatchType
from SystemEvent import Signature
from IosLogParser import LogLine

class SignatureTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('SignatureTest')
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        raw_data = '2013-03-22 22:17:52.317 MobileCalculator[22262:c07] Digit pressed: 8'
        year = 2013
        month = 03
        day = 22
        hour = 22
        minute = 17
        second = 52
        microsecond = 317000
        timestamp = datetime(year, month, day, hour, minute, second, microsecond)
        pid = 22262
        mach_port = 'c07'
        source = 'MobileCalculator'
        msg = 'Digit pressed: 8'
        self.log_line = LogLine(raw_data, timestamp, pid, mach_port, source, msg)
        self.logDetailedInfo('Input log line:', self.log_line)
        
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testIsMatch(self):
        match_type = MatchType.EXACT
        field_name = 'source'
        match_value = 'MobileCalculator'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isMatch(self.log_line)
        self.logDetailedInfo('Match:', match)
        
        assert match != None, 'Match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
     
    @log_test(logger, globals.log_separator)
    def testIsExactMatch(self):
        match_type = MatchType.EXACT
        field_name = 'source'
        match_value = 'MobileCalculator'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isExactMatch(self.log_line, True)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Exact match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsExactCaseInMatch(self):
        match_type = MatchType.EXACT_CASE_IN
        field_name = 'source'
        match_value = 'mobilecalculator'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isExactMatch(self.log_line, False)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Exact match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsStartsWithMatch(self):
        match_type = MatchType.STARTS_WITH
        field_name = 'source'
        match_value = 'Mobile'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isStartsWithMatch(self.log_line, True)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Starts with match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsStartsWithCaseInMatch(self):
        match_type = MatchType.STARTS_WITH_CASE_IN
        field_name = 'source'
        match_value = 'mobile'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isStartsWithMatch(self.log_line, False)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Starts with match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsEndsWithMatch(self):
        match_type = MatchType.ENDS_WITH
        field_name = 'source'
        match_value = 'Calculator'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isEndsWithMatch(self.log_line, True)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Ends with match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsEndsWithCaseInMatch(self):
        match_type = MatchType.ENDS_WITH_CASE_IN
        field_name = 'source'
        match_value = 'calculator'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isEndsWithMatch(self.log_line, False)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Ends with match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsContainsMatch(self):
        match_type = MatchType.CONTAINS
        field_name = 'source'
        match_value = 'leCal'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isContainsMatch(self.log_line, True)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Contains match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsContainsCaseInMatch(self):
        match_type = MatchType.CONTAINS_CASE_IN
        field_name = 'source'
        match_value = 'lecal'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isContainsMatch(self.log_line, False)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Contains match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsRegexMatch(self):
        match_type = MatchType.REGEX
        field_name = 'mach_port'
        match_value = '[a-zA-Z][0-9][0-9]'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isRegexMatch(self.log_line, True)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Regex match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    @log_test(logger, globals.log_separator)
    def testIsRegexCaseInMatch(self):
        match_type = MatchType.REGEX_CASE_IN
        field_name = 'mach_port'
        match_value = '[A-Z][0-9][0-9]'
        signature = Signature(match_type, field_name, match_value)
        self.logDetailedInfo('Signature:', signature)
        
        match = signature.isRegexMatch(self.log_line, False)
        self.logDetailedInfo('Match:', match)
        
        assert match != False, 'Regex match was not found in log line.'
        
        SignatureTest.logger.debug('Test succeeded!')
    
    def logDetailedInfo(self, title, log_line):
        log_line_str = str(log_line)
        SignatureTest.logger.debug(title)
        
        tokens = log_line_str.split('\t')
        for token in tokens:
            SignatureTest.logger.debug('\t' + token)
            
            
            
          
            
            
            
        