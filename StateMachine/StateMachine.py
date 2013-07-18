# ------------------------------------------------------
#
#   StateMachine.py
#   By: Fred Stakem
#   Created: 3.10.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

class StateMachine(object):
    """This class represents a state machine."""
    
    def __init__(self, name='Generic State Machine'):
        self.name = name
        self.states = []
        self.last_event = None
        self.current_state = None
        
    def setUpStates(self, states):
        if len(states) > 0:
            self.states = states
            self.current_state = self.states[0]
        else:
            pass
        
    def handleTransition(self, transition_event):
        if self.current_state == None:
            pass
        
        self.current_state.handleTransition(transition_event)
        self.last_event = transition_event
    
    
    
    
    