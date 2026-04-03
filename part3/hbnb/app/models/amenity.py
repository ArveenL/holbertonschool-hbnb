from app import db
from app.models.baseModel import BaseModel

class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(100), nullable=False)  # Name of the amenity