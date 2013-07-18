# ------------------------------------------------------
#
#   Symbol.py
#   By: Fred Stakem
#   Created: 3.9.13
#
# ------------------------------------------------------


# Libs

# User defined
import Utilities

class Symbol(object):
    """This class represents a symbol for mapping characters to internal representation."""
       
    # Setup logging
    logger = Utilities.getLogger('LogParser::Symbol')
    
    # Class constants
    symbol_table = {
                    'unknown':              [],
                    'separator':            [ ' ', '\t' ],
                    'hash':                 [ '#' ],          
                    'eol':                  [ '\n' ],
                    'eof':                  [ 'eof' ],
                    'dash':                 [ '-' ],
                    'underscore':           [ '_' ],
                    'tilda':                [ '~' ],
                    'char':                 [],
                    'digit':                [],
                    'single quote':         [ "'" ],
                    'double quote':         [ '"' ],
                    'left curly brace':     [ '{' ],
                    'right curly brace':    [ '}' ],
                    'left brace':           [ '[' ],
                    'right brace':          [ ']' ],
                    'dot':                  [ '.' ],
                    'colon':                [ ':' ],
                    'exponent':             [ 'e', 'E' ],
                    'bar':                  [ '|' ],
                    'forward_slash':        [ '/' ],
                    'backward_slash':       [ '\\' ]
                   }
    
    keywords = {
                'boolean true':             [ 'true' ],
                'boolean false':            [ 'false' ]
               }
    
    UNKNOWN = symbol_table['unknown']
    SEPARATOR = symbol_table['separator']
    HASH = symbol_table['hash']
    EOL = symbol_table['eol']
    EOF = symbol_table['eof']
    DASH = symbol_table['dash']
    UNDERSCORE = symbol_table['underscore']
    TILDA = symbol_table['tilda']
    CHAR = symbol_table['char']
    DIGIT = symbol_table['digit']
    SINGLE_QUOTE = symbol_table['single quote']
    DOUBLE_QUOTE = symbol_table['double quote']
    LEFT_CURLY_BRACE = symbol_table['left curly brace']
    RIGHT_CURLY_BRACE = symbol_table['right curly brace']
    LEFT_BRACE = symbol_table['left brace']
    RIGHT_BRACE = symbol_table['right brace']
    DOT = symbol_table['dot']
    COLON = symbol_table['colon']
    EXPONENT = symbol_table['exponent']
    BAR = symbol_table['bar'] 
    FORWARD_SLASH = symbol_table['forward_slash']
    BACKWARD_SLASH = symbol_table['backward_slash']
    
    BOOLEAN_TRUE = keywords['boolean true']
    BOOLEAN_FALSE = keywords['boolean false']
    
    def __init__(self):
        pass
    
    @classmethod
    def isSeparator(cls, symbol):
        return cls.isMatch(symbol, cls.SEPARATOR)
        
    @classmethod
    def isHash(cls, symbol):
        return cls.isMatch(symbol, cls.HASH)
        
    @classmethod
    def isEol(cls, symbol):
        return cls.isMatch(symbol, cls.EOL)
        
    @classmethod
    def isEof(cls, symbol):
        return cls.isMatch(symbol, cls.EOF)
        
    @classmethod
    def isDash(cls, symbol):
        return cls.isMatch(symbol, cls.DASH)
        
    @classmethod
    def isUnderscore(cls, symbol):
        return cls.isMatch(symbol, cls.UNDERSCORE)
        
    @classmethod
    def isTilda(cls, symbol):
        return cls.isMatch(symbol, cls.TILDA)
        
    @classmethod
    def isCharacter(cls, symbol):
        return symbol.isalpha()
        
    @classmethod
    def isDigit(cls, symbol):
        return symbol.isdigit()
        
    @classmethod
    def isQuote(cls, symbol, quote_type):
        return cls.isMatch(symbol, quote_type)
        
    @classmethod
    def isSingleQuote(cls, symbol):
        return cls.isMatch(symbol, cls.SINGLE_QUOTE)
        
    @classmethod
    def isDoubleQuote(cls, symbol):
        return cls.isMatch(symbol, cls.DOUBLE_QUOTE)
        
    @classmethod
    def isLeftCurlyBrace(cls, symbol):
        return cls.isMatch(symbol, cls.LEFT_CURLY_BRACE)
        
    @classmethod
    def isRightCurlyBrace(cls, symbol):
        return cls.isMatch(symbol, cls.RIGHT_CURLY_BRACE)
        
    @classmethod
    def isLeftBrace(cls, symbol):
        return cls.isMatch(symbol, cls.LEFT_BRACE)
        
    @classmethod
    def isRightBrace(cls, symbol):
        return cls.isMatch(symbol, cls.RIGHT_BRACE)
        
    @classmethod
    def isDot(cls, symbol):
        return cls.isMatch(symbol, cls.DOT)
        
    @classmethod
    def isColon(cls, symbol):
        return cls.isMatch(symbol, cls.COLON)
        
    @classmethod
    def isExponent(cls, symbol):
        return cls.isMatch(symbol, cls.EXPONENT)
        
    @classmethod
    def isBar(cls, symbol):
        return cls.isMatch(symbol, cls.BAR)
    
    @classmethod
    def isForwardSlash(cls, symbol):
        return cls.isMatch(symbol, cls.FORWARD_SLASH)
    
    @classmethod
    def isBackwardSlash(cls, symbol):
        return cls.isMatch(symbol, cls.BACKWARD_SLASH)
        
    @classmethod
    def isBooleanTrue(cls, token):
        return cls.isMatch(token, cls.BOOLEAN_TRUE)
        
    @classmethod
    def isBooleanFalse(cls, token):
        return cls.isMatch(token, cls.BOOLEAN_FALSE)
    
    @classmethod 
    def isMatch(cls, value, value_list):
        result = False
        for other_value in value_list:
            if value == other_value:
                result = True
                break
            
        return result
            
    
    
    
    