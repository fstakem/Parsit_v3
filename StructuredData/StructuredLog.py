# ------------------------------------------------------
#
#   StructuredLog.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Metadata import Metadata
from StructuredLogSample import StructuredLogSample

class StructuredLog(object):
    """This class represents a structured log where structured data is held."""
    
    def __init__(self, name='Generic structured log', events=[], metadata=Metadata()):
        self.name = name
        self.events = events
        self.metadata = metadata
        
    def __str__(self):
        output = 'Log name: %s\tNumber of events: %d\tMetadata: %s' % \
                 (self.name, len(self.events), str(self.metadata))
        return output
    
    def __repr__(self):
        return str(self)
    
    def findEventsInLog(self, name, log):
        log_sample = StructuredLogSample(name, self, log)
        log_sample.findEventsInLog()
            
        return log_sample