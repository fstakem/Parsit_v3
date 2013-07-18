# ------------------------------------------------------
#
#   StateTransition.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

class StateTransition(object):
    """This class represents a state transition of a state machine."""
    
    def __init__(self, name='Generic Transition'):
        self.name = name
        self.transition_event = None
        self.enter_event = None
        self.exit_event = None
        
    def __equ__(self, other):
        pass
    
    def __ne__(self, other):
        pass
        
    def __str__(self):
        pass
    
    def __repr__(self):
        return str(self)
    
    
    
    