from app import db
from app.models.baseModel import BaseModel

class Review(BaseModel):
    __tablename__ = "reviews"

    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), nullable=False)
    place_id = db.Column(db.String(36), nullable=False)