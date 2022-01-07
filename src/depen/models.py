from sqlalchemy import Time, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship



from .database import Base ,engine


class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String , nullable=False,index=True)
    qr_id= Column(Integer , index=True)

    talks = relationship('Talk', cascade="all,delete",passive_deletes=True,back_populates='speaker')
    

class Talk(Base):
    __tablename__ = "talks"

    id = Column(Integer , primary_key=True, index=True)
    subject = Column(String, index=True)

    start_time = Column(Time)
    end_time = Column(Time)

    path = Column(String)
    file = Column(String)

    speaker_id = Column(Integer , ForeignKey('speakers.id', ondelete="CASCADE"))
    speaker = relationship('Speaker',back_populates='talks')

    session_id = Column(Integer , ForeignKey('sessions.id', ondelete="CASCADE"))
    session = relationship('Session',back_populates='talks')


class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    date = Column(Date)

    path = Column(String)

    talks = relationship('Talk', cascade="all,delete",passive_deletes=True,back_populates='session')
    
    hall_id = Column(Integer, ForeignKey("halls.id", ondelete="CASCADE"))
    hall = relationship("Hall", back_populates="sessions")



class Hall(Base):
    __tablename__ = "halls"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    start_date = Column(Date)
    end_date = Column(Date)

    path = Column(String)

    sessions = relationship("Session", cascade="all,delete",passive_deletes=True, back_populates="hall")

    conf_id = Column(Integer , ForeignKey('conferances.id' , ondelete="CASCADE"))
    conf = relationship("Conferance", back_populates="halls")

class Conferance(Base):
    __tablename__ = "conferances"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    start_date = Column(Date)
    end_date = Column(Date)

    path = Column(String)

    halls = relationship("Hall" ,cascade="all, delete",passive_deletes=True, back_populates="conf")


Base.metadata.create_all(bind=engine)