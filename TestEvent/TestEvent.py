# ------------------------------------------------------
#
#   TestEvent.py
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
from IosLogParser import LogLine
from SystemEvent import Event
from SystemEvent import EventType
from SystemEvent import Metadata
from SystemEvent import Signature
from SystemEvent import MatchType

class EventTest(unittest.TestCase):
    
    # Setup logging
    logger = Utilities.getLogger('EventTest')
    
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
    def testGetSignatureMatches(self):
        event_name = 'Test Event'
        event_type = EventType.GENERIC
        match_type = MatchType.EXACT
        field_name = 'source'
        match_value = 'MobileCalculator'
        signature = Signature(match_type, field_name, match_value)
        signatures = [signature]
        metadata = Metadata()
        event = Event(event_name, event_type, signatures, metadata)
        self.logDetailedInfo('Event:', event)
        
        matches = event.getSignatureMatches(self.log_line)
        for match in matches:
            self.logDetailedInfo('Match:', match)
        
        assert len(matches) > 0, 'Match was not found in log line.'
        
        EventTest.logger.debug('Test succeeded!')
        
    def logDetailedInfo(self, title, log_line):
        log_line_str = str(log_line)
        EventTest.logger.debug(title)
        
        tokens = log_line_str.split('\t')
        for token in tokens:
            EventTest.logger.debug('\t' + token)
    
     