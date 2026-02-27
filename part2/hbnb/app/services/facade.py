from app.models.user import User
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        # One repository for users
        self.user_repo = InMemoryRepository()

    # -------------------------
    # CREATE
    # -------------------------
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # -------------------------
    # GET ONE
    # -------------------------
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # -------------------------
    # GET ALL
    # -------------------------
    def get_all_users(self):
        return self.user_repo.get_all()

    # -------------------------
    # GET BY EMAIL
    # -------------------------
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    # -------------------------
    # UPDATE
    # -------------------------
    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        # Update only allowed fields
        if "first_name" in user_data:
            user.first_name = user_data["first_name"]
        if "last_name" in user_data:
            user.last_name = user_data["last_name"]
        if "email" in user_data:
            user.email = user_data["email"]

        return user


# Create a single facade instance used by the API
facade = HBnBFacade()
