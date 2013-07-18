# ------------------------------------------------------
#
#   Metadata.py
#   By: Fred Stakem
#   Created: 4.20.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

class Metadata(object):
    """This class represents a meta data for an event."""
    
    def __init__(self):
        pass
    
    def __str__(self):
        variables = vars(self)
        output = ''
        
        for name, value in variables.iteritems():
            output += 'Var name: %s\tVar value: %s\t' % (name. str(value))
            
        output = output[:-1]
        
        return output
    
    def __repr__(self):
        return str(self)