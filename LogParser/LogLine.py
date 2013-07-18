# ------------------------------------------------------
#
#   LogLine.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------

# Libs
# None

# User defined
# None

class LogLine(object):
    """This class represents a log line where parsed data is held."""
    
    def __init__(self, raw_data=''):
        self.raw_data = raw_data