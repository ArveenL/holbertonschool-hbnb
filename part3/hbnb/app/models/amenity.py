from app import db
from app.models.baseModel import BaseModel


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(50), nullable=False)

    # Relationship with Place
    places = db.relationship(
        'Place',
        secondary='place_amenity',
        lazy='subquery',
        backref=db.backref('amenities', lazy=True)
    )