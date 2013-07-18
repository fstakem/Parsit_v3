# ------------------------------------------------------
#
#   Log.py
#   By: Fred Stakem
#   Created: 6.6.13
#
# ------------------------------------------------------


# Libs
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# User defined
from Database import Base

class Log(Base):
    __tablename__ = 'logs'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    metadata_loc = Column(String)
    user_handle = Column(String, unique=True)
    data = relationship('LogData')
    
    def __init__(self, name=None, metadata_loc=None, user_handle=None):
        self.name = name
        self.metadata_loc = metadata_loc
        self.user_handle = user_handle
        
    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return "<Log('%s', '%s', '%s')>" % (self.name, self.metadata_loc, self.user_handle) 


