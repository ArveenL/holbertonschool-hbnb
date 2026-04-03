from app import db
import uuid
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # SQLAlchemy won't create a table for BaseModel

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Save object to the database"""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Update object attributes"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()