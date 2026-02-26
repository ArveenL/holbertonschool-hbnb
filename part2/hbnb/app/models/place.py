from app.models.baseModel import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner: 'User'):
        super().__init__()
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) > 100:
            raise ValueError("title must not be more than 100 characters")
        self.title = title
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a number")
        self.price = price
        if not isinstance(latitude, (float, int)):
            raise TypeError("latitude must be a number")
        if latitude > 90 or latitude < -90:
            raise ValueError("latitude must be between -90 and 90")
        self.latitude = latitude
        if not isinstance(longitude, (float, int)):
            raise TypeError("longitude must be a number")
        if longitude > 180 or longitude < -180:
            raise ValueError("longitude must be between -180 and 180")
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)

    def add_review(self, review: 'Review'):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity: 'Amenity'):
        """Add an amenity to the place."""
        self.amenities.append(amenity)