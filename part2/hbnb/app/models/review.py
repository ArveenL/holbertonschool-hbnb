from app.models.baseModel import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place: 'Place', user: 'User'):
        super().__init__()
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        if not isinstance(rating, int):
            raise TypeError("rating must be an integer")
        if rating not in range(1, 6):
            raise ValueError("rating must be between 1 and 5")
        self.rating = rating
        self.place = place
        self.user = user

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)
