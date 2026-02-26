from baseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)
