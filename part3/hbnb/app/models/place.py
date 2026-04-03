from app import db
from app.models.baseModel import BaseModel

class Place(BaseModel):
    __tablename__ = "places"

    # core attributes
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(36), nullable=False)