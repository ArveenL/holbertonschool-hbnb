from baseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) > 50:
            raise ValueError("name must not be more than 50 characters")
        self.name = name

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)
