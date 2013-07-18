# ------------------------------------------------------
#
#   Event.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from EventType import EventType
from Metadata import Metadata

class Event(object):
    """This class represents an event."""
    
    def __init__(self, name='Generic Event', event_type=EventType.NONE, signatures=[], metadata=Metadata()):
        self.name = name
        self.event_type = event_type
        self.signatures = signatures
        self.metadata = metadata
            
    def __str__(self):
        output = 'Event name: %s\tType: %s\t' % (self.name, EventType.prettyPrint(self.event_type))
        for i, signature in enumerate(self.signatures):
            output += 'Signature(%d):\t%s\t' % ( (i+1), str(signature) )
        output += 'Metadata: %s' % (str(self.metadata))
        return output
    
    def __repr__(self):
        return str(self)
    
    def getSignatureMatches(self, log_line):
        matches = []
        
        for signature in self.signatures:
            match = signature.isMatch(log_line)
            
            if match != None:
                matches.append(match)
        
        return matches
    
 
    
    
    
    