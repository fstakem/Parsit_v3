# ------------------------------------------------------
#
#   TestStructuredLogSample.py
#   By: Fred Stakem
#   Created: 5.5.13
#
# ------------------------------------------------------


# Libs
import unittest
from datetime import datetime

# User defined
from Utilities import *
from Globals import *
from LogParser import LogSource
from IosLogParser import Scanner
from IosLogParser import Parser
from IosLogParser import LogLine
from SystemEvent import Event
from SystemEvent import EventType
from SystemEvent import Signature
from SystemEvent import MatchType
from SystemEvent import Metadata as EventMetadata
from StructuredData import Metadata as StructuredDataMetadata
from StructuredData import StructuredLogSample
from StructuredData import StructuredLog

class StructuredLogSampleTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('StructuredLogSampleTest')
    data_file = '../data/iphone_log_2.txt'
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.log = None
        self.log_errors = None
        self.getDataFromLog(StructuredLogSampleTest.data_file)
        
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testFindEventsInLog(self):
        structured_log_name = 'Test structured log'
        event_name = 'Pressed 4 button'
        event_type = EventType.GENERIC
        match_type = MatchType.CONTAINS
        field_name = 'msg'
        expected_value = '4'
        signatures = [ Signature(match_type, field_name, expected_value) ]
        metadata = EventMetadata()
        events = [ Event(event_name, event_type, signatures, metadata) ]
        metadata = StructuredDataMetadata()
        structured_log = StructuredLog(structured_log_name, events, metadata)
        self.logDetailedInfo('Structured log:', structured_log)
        
        structured_log_sample_name = 'Test structured log sample'
        structured_log_sample = StructuredLogSample(structured_log_sample_name, structured_log, self.log)
        self.logDetailedInfo('Structured log sample:', structured_log_sample)
        
        structured_log_sample.findEventsInLog()
        found_events = structured_log_sample.event_matches
        StructuredLogSampleTest.logger.debug('Found %d matches in the log.' % (len(found_events)))
        
        assert len(found_events) == 2, 'Incorrect number of matches found in the log.'
        
        StructuredLogSampleTest.logger.debug('Test succeeded!')
        
    def getDataFromLog(self, data_file):
        source = LogSource('iOS Test Source', None)
        scanner = Scanner('iOS Test Scanner', source)
        parser = Parser('iOS Test Parser', scanner)
        
        StructuredLogSampleTest.logger.debug('Importing data in the file: ' + data_file)
        lines = readLinesFromFile(data_file)
        
        for line in lines:
            line += '\n'
            
        self.log, self.log_errors = parser.parse('Test iOS Log', lines)
        
        if len(self.log_errors) != 0:
            assert False, 'Error parsing test data file.'
        
    def logDetailedInfo(self, title, log_line):
        log_line_str = str(log_line)
        StructuredLogSampleTest.logger.debug(title)
        
        tokens = log_line_str.split('\t')
        for token in tokens:
            StructuredLogSampleTest.logger.debug('\t' + token)
    
     