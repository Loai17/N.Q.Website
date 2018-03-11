from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


class Emails(Base):
	__tablename__ = 'emails'
	id = Column(Integer,primary_key=True)
	email = Column(String)
	name = Column (String) 

# chris = Emails(email= "Any@Email.com", name = "Chris Issa")
# session.add(chris)
# session.commit()

Base.metadata.create_all(engine)