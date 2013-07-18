# ------------------------------------------------------
#
#   Signature.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------


# Libs
import re

# User defined
from Match import Match
from MatchType import MatchType

class Signature(object):
    """This class represents a signature for an event."""
    
    def __init__(self, match_type=MatchType.NONE, field_name='name', expected_value=None):
        self.match_type = match_type
        self.field_name = field_name
        self.expected_value = expected_value
    
    def __str__(self):
        output = 'Match type: %s\t' % ( MatchType.prettyPrint(self.match_type) )
        output += 'Field name: %s\tExpected value: %s' % (self.field_name, str(self.expected_value))
        return output
    
    def __repr__(self):
        return str(self)
    
    def isMatch(self, log_line):
        is_match = False
        
        if self.match_type == MatchType.EXACT:
            is_match = self.isExactMatch(log_line, True)
        elif self.match_type == MatchType.EXACT_CASE_IN:
            is_match = self.isExactMatch(log_line, False)
        elif self.match_type == MatchType.STARTS_WITH:
            is_match = self.isStartsWithMatch(log_line, True)
        elif self.match_type == MatchType.STARTS_WITH_CASE_IN:
            is_match = self.isStartsWithMatch(log_line, False)
        elif self.match_type == MatchType.ENDS_WITH:
            is_match = self.isEndsWithMatch(log_line, True)
        elif self.match_type == MatchType.ENDS_WITH_CASE_IN:
            is_match = self.isEndsWithMatch(log_line, False)
        elif self.match_type == MatchType.CONTAINS:
            is_match = self.isContainsMatch(log_line, True)
        elif self.match_type == MatchType.CONTAINS_CASE_IN:
            is_match = self.isContainsMatch(log_line, False)
        elif self.match_type == MatchType.REGEX:
            is_match = self.isRegexMatch(log_line, True)
        elif self.match_type == MatchType.REGEX_CASE_IN:
            is_match = self.isRegexMatch(log_line, False)
            
        if is_match:
            return Match(self.match_type, log_line)
            
        return None
    
    def isExactMatch(self, log_line, case_sensitive):
        log_value = self.getValue(log_line)
        
        if log_value == None:
            return False
        
        if type(self.expected_value) == str and type(log_value) == str and not case_sensitive:
            if log_value.lower() == self.expected_value.lower():
                return True
        elif log_value == self.expected_value:
            return True
        
        return False
    
    def isStartsWithMatch(self, log_line, case_sensitive):
        log_value = self.getValue(log_line)
        
        if log_value == None:
            return False
        
        if type(self.expected_value) == str and type(log_value) == str:
            if not case_sensitive:
                if log_value.lower().startswith(self.expected_value.lower()):
                    return True
            else:
                if log_value.startswith(self.expected_value):
                    return True
            
        return False
    
    def isEndsWithMatch(self, log_line, case_sensitive):
        log_value = self.getValue(log_line)
        
        if log_value == None:
            return False
        
        if type(self.expected_value) == str and type(log_value) == str:
            if not case_sensitive:
                if log_value.lower().endswith(self.expected_value.lower()):
                    return True
            else:
                if log_value.endswith(self.expected_value):
                    return True
            
        return False
    
    def isContainsMatch(self, log_line, case_sensitive):
        log_value = self.getValue(log_line)
        
        if log_value == None:
            return False
        
        if type(self.expected_value) == str and type(log_value) == str:
            if not case_sensitive:
                if log_value.lower().find(self.expected_value.lower()) != -1:
                    return True
            else:
                if log_value.find(self.expected_value) != -1:
                    return True
            
        return False
    
    def isRegexMatch(self, log_line, case_sensitive):
        log_value = self.getValue(log_line)
        
        if log_value == None:
            return False
        
        if type(self.expected_value) == str and type(log_value) == str:
            regex = None
            if not case_sensitive:
                regex = re.compile(self.expected_value, re.IGNORECASE)
            else:
                regex = re.compile(self.expected_value)
                
            matches = regex.findall(log_value)
            
            if len(matches) > 0:
                return True
            
        return False
    
    def getValue(self, log_line):
        try:
            return log_line.__getattribute__(self.field_name)
        except AttributeError:
            return None
    
    
    
    
    
    
    
    
    
    
    
    
        
        