from app.models.baseModel import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin = False):
        super().__init__()
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if len(first_name) > 50:
            raise ValueError("first_name must not be more than 50 characters")
        self.first_name = first_name
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if len(last_name) > 50:
            raise ValueError("last_name must not be more than 50 characters")
        self.last_name = last_name
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        #TODO verify email
        self.email = email
        if not isinstance(is_admin, bool):
            raise TypeError("is_admin must be a boolean")
        self.is_admin = is_admin
        self.places = []

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)

    def add_place(self, place):
        """Add a Place to the User."""
        self.places.append(place)