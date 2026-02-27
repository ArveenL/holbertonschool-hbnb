from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # -------------------------
    # USER METHODS
    # -------------------------

    # Create user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Get single user
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # Get all user
    def get_all_users(self):
        return self.user_repo.get_all()

    # Get user by email
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    # update user
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

    # -------------------------
    # AMENITY METHODS
    # -------------------------

    # Create amenity
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    # Get single amenity
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    # Get all amenities
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # Update amenity
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)

        if not amenity:
            return None

        for key, value in amenity_data.items():
            setattr(amenity, key, value)

        return amenity

    # -------------------------
    # PLACE METHODS
    # -------------------------

    def create_place(self, place_data):
        owner = self.get_user(place_data['owner_id'])
        if owner is None:
            return None
        place_data.update({"owner": owner})
        place_data.pop("owner_id")

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place is None:
            return None
        for key, value in place_data.items():
            setattr(place, key, value)
        return place

    # -------------------------
    # REVIEW METHODS
    # -------------------------

    def create_review(self, review_data):
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])
        if user is None or place is None:
            return None
        review_data.update({"user": user})
        review_data.update({"place": place})
        review_data.pop("user_id")
        review_data.pop("place_id")
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        return self.place_repo.get("place", place)

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if review is None:
            return None
        for key, value in review_data.items():
            setattr(review, key, value)
        return review

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)


# Create a single facade instance used by the API
facade = HBnBFacade()
