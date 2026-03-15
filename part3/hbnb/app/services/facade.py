from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import UserRepository, SQLAlchemyRepository


class HBnBFacade:
    def __init__(self):
        # User operations use dedicated repository
        self.user_repo = UserRepository()

        # Other entities use SQLAlchemyRepository
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    # -------------------------
    # USER METHODS
    # -------------------------
    def create_user(self, user_data):
        user = User(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            is_admin=user_data.get("is_admin", False)
        )
        user.hash_password(user_data["password"])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        for field in ["first_name", "last_name", "email"]:
            if field in user_data:
                setattr(user, field, user_data[field])
        if "password" in user_data:
            user.hash_password(user_data["password"])
        self.user_repo.update(user_id, {})  # commit
        return user

    # -------------------------
    # PLACE METHODS
    # -------------------------
    def create_place(self, place_data):
        owner = self.get_user(place_data['user_id'])
        if not owner:
            return None
        place = Place(
            title=place_data["title"],
            description=place_data["description"],
            price=place_data["price"],
            latitude=place_data["latitude"],
            longitude=place_data["longitude"],
            user_id=owner.id  # link to owner
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            setattr(place, key, value)
        self.place_repo.update(place_id, {})
        return place

    # -------------------------
    # REVIEW METHODS
    # -------------------------
    def create_review(self, review_data):
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])
        if not user or not place:
            return None
        review = Review(
            text=review_data["text"],
            rating=review_data["rating"],
            user_id=user.id,
            place_id=place.id
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            return None
        return self.review_repo.get_all_by_attribute("place_id", place.id)

    def get_reviews_by_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            return None
        return self.review_repo.get_all_by_attribute("user_id", user.id)

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            setattr(review, key, value)
        self.review_repo.update(review_id, {})
        return review

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

    # -------------------------
    # AMENITY METHODS
    # -------------------------
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        for key, value in amenity_data.items():
            setattr(amenity, key, value)
        self.amenity_repo.update(amenity_id, {})
        return amenity

    # -------------------------
    # PLACE ↔ AMENITY METHODS
    # -------------------------
    def add_amenity_to_place(self, place_id, amenity_id):
        place = self.get_place(place_id)
        amenity = self.get_amenity(amenity_id)
        if not place or not amenity:
            return None
        place.amenities.append(amenity)
        self.place_repo.update(place_id, {})
        return place


# Single facade instance
facade = HBnBFacade()