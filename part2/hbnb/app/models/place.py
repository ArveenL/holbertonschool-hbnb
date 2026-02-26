from baseModel import BaseModel
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) > 100:
            raise ValueError("title must not be more than 100 characters")
        self.title = title
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description
        if not isinstance(price, float):
            raise TypeError("price must be a number")
        self.price = price
        if not isinstance(latitude, str):
            raise TypeError("latitude must be a number")
        if latitude > 90 or latitude < -90:
            raise ValueError("latitude must be between -90 and 90")
        self.latitude = latitude
        if not isinstance(longitude, str):
            raise TypeError("longitude must be a number")
        if longitude > 180 or longitude < -180:
            raise ValueError("longitude must be between -180 and 180")
        self.longitude = longitude
        if not isinstance(title, User):
            raise TypeError("owner must be a User")
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)

    def add_review(self, review):
        """Add a review to the place."""
        if not isinstance(review, Review):
            raise TypeError("review must be a Review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise TypeError("amenity must be an Amenity")
        self.amenities.append(amenity)