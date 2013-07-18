# ------------------------------------------------------
#
#   Database.py
#   By: Fred Stakem
#   Created: 6.6.13
#
# ------------------------------------------------------


# Libs
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# User defined
# None

engine = create_engine('sqlite:///../upload/log_data.db', convert_unicode=True, echo=True)
db_session = scoped_session( sessionmaker(autocommit=False, autoflush=False, bind=engine) )
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import Log
    import LogData
    Base.metadata.create_all(bind=engine)
