# ------------------------------------------------------
#
#   StructuredLogSample.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from LogParser import Log

class StructuredLogSample(object):
    """This class represents a structured log sample where structured data is held."""
    
    def __init__(self, name='Generic structured log sample', structured_log=None, log=Log()):
        self.name = name
        self.structured_log = structured_log
        self.log = log
        self.event_matches = []
        
    def __str__(self):
        output = 'Log sample name: %s\tLog: %s\tNumber of event found: %d' % \
                 (self.name, str(self.structured_log), len(self.event_matches))
        return output
    
    def __repr__(self):
        return str(self)
    
    def findEventsInLog(self):
        self.event_matches = []
        
        for line in self.log.lines:
            for event in self.structured_log.events:
                for signature in event.signatures:
                    match = signature.isMatch(line)
                    if match != None:
                        self.event_matches.append(match)
                
    