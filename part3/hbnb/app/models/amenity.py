from app import db
from app.models.baseModel import BaseModel

class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(200), nullable=False)