# ------------------------------------------------------
#
#   LogLine.py
#   By: Fred Stakem
#   Created: 3.23.13
#
# ------------------------------------------------------


# Libs
import datetime

# User defined
from LogParser import LogLine as BaseLogLine

class LogLine(BaseLogLine):
    
    def __init__(self, raw_data='', timestamp=datetime.datetime.now(), pid=-1, 
                 mach_port=-1, source='Main', msg='iOS log msg.'):
        super(LogLine, self).__init__(raw_data)
        self.timestamp = timestamp
        self.source = source
        self.pid = pid
        self.mach_port = mach_port
        self.msg = msg
    
    def __str__(self):
        return str(self.timestamp) + '\t' + str(self.pid) + '\t' + \
               str(self.mach_port) +  '\t' + str(self.source) + '\t' + \
               self.msg
                  
    def __repr__(self):
        return str(self)
    
    
    
    