# ------------------------------------------------------
#
#   State.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

class State(object):
    """This class represents a state of a state machine."""
    
    def __init__(self, name='Generic State', state_machine=None, transition_table=[]):
        self.name = ''
        self.state_machine = state_machine
        self.transition_table = transition_table
        
    def handleTransition(self, transition_event):
        pass
    
    def enter(self):
        pass
    
    def exit(self):
        pass
    
    
    
    