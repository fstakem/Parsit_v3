# ------------------------------------------------------
#
#   Log.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from LogParser import Log as BaseLog

class Log(BaseLog):
    
    def __init__(self, name='Android Log', lines=[]):
        self.name = name
        self.lines = lines
    
    def __str__(self):
        return 'Log: ' + self.name + ' has ' + str(len(self.lines)) + ' lines.'
    
    def __repr__(self):
        return str(self)