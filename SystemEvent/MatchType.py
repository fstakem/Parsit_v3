# ------------------------------------------------------
#
#   MatchType.py
#   By: Fred Stakem
#   Created: 4.26.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

class MatchType(object):
    """This class represents a match type that is found if a log line matches a signature."""
       
    # Class constants
    NONE = 0
    EXACT = 1
    EXACT_CASE_IN = 2
    STARTS_WITH = 3
    STARTS_WITH_CASE_IN = 4
    ENDS_WITH = 5
    ENDS_WITH_CASE_IN = 6
    CONTAINS = 7
    CONTAINS_CASE_IN = 8
    REGEX = 9
    REGEX_CASE_IN = 10
    
    readable_name = {
                     NONE:                      'None',
                     EXACT:                     'Exact match',
                     EXACT_CASE_IN:             'Exact match case insensitive',
                     STARTS_WITH:               'Starts with',
                     STARTS_WITH_CASE_IN:       'Starts with case insensitive',
                     ENDS_WITH:                 'Ends with',
                     ENDS_WITH_CASE_IN:         'Ends with case insensitive',
                     CONTAINS:                  'Contains',
                     CONTAINS_CASE_IN:          'Contains case insensitive',
                     REGEX:                     'Regex',
                     REGEX_CASE_IN:             'Regex case insensitive',
                    }
    
    @classmethod
    def prettyPrint(cls, token_type):
        return cls.readable_name[token_type]
    
   
    
    
    
    