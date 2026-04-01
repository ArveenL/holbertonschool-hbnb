from app import db
from app.models.baseModel import BaseModel

# Association table for Place <-> Amenity
place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(50), nullable=False)

    # Relationship with Place
    places = db.relationship(
        'Place',
        secondary=place_amenity,
        lazy='subquery',
        backref=db.backref('amenities', lazy=True)
    )