# ------------------------------------------------------
#
#   Match.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from LogParser import LogLine
from MatchType import MatchType

class Match(object):
    """This class represents a match of an event."""
    
    def __init__(self, match_type=MatchType.NONE, log_line=LogLine()):
        self.match_type = match_type
        self.log_line = log_line
        self.line_number = 0
        self.event = None
        
    def __str__(self):
        type_str = MatchType.prettyPrint(self.match_type)
        log_line_str = ' '.join( str(self.log_line).split('\t') )
        output = 'Type: %s\tLog line:%s\tLine number:%s\tEvent:%s' % \
                 (type_str, log_line_str, str(self.line_number), str(self.event))
        return output
    
    def __repr__(self):
        return str(self)