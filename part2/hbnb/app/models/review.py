from app.models.baseModel import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        if not isinstance(rating, int):
            raise TypeError("rating must be an integer")
        if rating not in range(1, 6):
            raise ValueError("rating must be between 1 and 5")
        self.rating = rating
        if not isinstance(place, Place):
            raise TypeError("title must be a string")
        self.place = place
        if not isinstance(user, User):
            raise TypeError("amenity must be an Amenity")
        self.user = user

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)
