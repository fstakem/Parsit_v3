# ------------------------------------------------------
#
#   LogLine.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------


# Libs
import datetime

# User defined
import Utilities
from LogParser import LogLine as BaseLogLine

LogLevel = Utilities.enum('Verbose', 'Info', 'Debug', 'Warn', 'Error', 'Assert')

class LogLine(BaseLogLine):
    
    def __init__(self, raw_data='', timestamp=datetime.datetime.now(), pid=-1, 
                 tid=-1, level=LogLevel.Verbose, source='Main', 
                 msg='Android log msg.'):
        super(LogLine, self).__init__(raw_data)
        self.timestamp = timestamp
        self.pid = pid
        self.tid = tid
        self.level = level
        self.source = source
        self.msg = msg
    
    def __str__(self):
        return str(self.timestamp) + '\t' + str(self.pid) + '\t' + \
               str(self.tid) + '\t' + str(self.level) + '\t' + \
               str(self.source) + '\t'  + self.msg
                  
    def __repr__(self):
        return str(self)
    
    
    
    