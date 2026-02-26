from baseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)
