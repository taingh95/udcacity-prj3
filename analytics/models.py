from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from config import db

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    joined_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    def __repr__(self):
        return "<User %r>" % self.id
class Token(db.Model):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(6), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    used_at = Column(DateTime)
    def __repr__(self):
        return "<Token %r>" % self.id