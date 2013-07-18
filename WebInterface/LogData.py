# ------------------------------------------------------
#
#   LogData.py
#   By: Fred Stakem
#   Created: 6.6.13
#
# ------------------------------------------------------


# Libs
from sqlalchemy import Column, Integer, String, ForeignKey

# User defined
from Database import Base
from Log import Log

class LogData(Base):
    __tablename__ = 'log_data_sets'
    
    id = Column(Integer, primary_key=True)
    log_loc = Column(String)
    user_handle = Column(String)
    parent_id = Column(Integer, ForeignKey('logs.id'))
    
    
    def __init__(self, log_loc=None, user_handle=None):
        self.log_loc = log_loc
        self.user_handle = user_handle
        
    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return "<LogData('%s', '%s')>" % (self.log_loc, self.user_handle)
    
    
    
    