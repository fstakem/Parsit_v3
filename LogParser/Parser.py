# ------------------------------------------------------
#
#   Parser.py
#   By: Fred Stakem
#   Created: 3.3.13
#
# ------------------------------------------------------

# Libs
# None

# User defined
# None

class Parser(object):
    """This class represents a parser to parse log files."""
    
    def __init__(self, name, scanner):
        self.name = name
        self.scanner = scanner
        self.current_token = None
        self.parsed_lines = []
        self.errors = []
        
    def parse(self):
        pass
    
    def __str__(self):
        output = 'Parser: %s\n' % (self.name)
        output += 'Current token: %s\n' % (self.current_token)
        output += 'Number of parsed lines: %s\n' % (str(len(self.parsed_lines)))
        for i, line in enumerate(self.parsed_lines):
            output += 'Parsed line %d: %s\n' % (i+1, str(line))
        output += 'Number of errors: %s\n' % (str(len(self.errors)))
        for i, error in enumerate(self.errors):
            output += 'Error %d: %s\n' % (i+1, str(error[3]))
        
        return output
    
    def parallelParse(self):
        pass
    
    def reset(self):
        self.scanner.reset()
    
    def parseLogLine(self, log_line):
        pass