from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///db.sqlite3', echo=True)
session = Session(bind=engine)

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

Base.metadata.create_all(engine)