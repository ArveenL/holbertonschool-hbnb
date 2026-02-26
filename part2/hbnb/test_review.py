from app.models.review import Review
from app.models.place import Place
from app.models.user import User

def test_review_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place("house", "it's a house", 100, 50.0, -100.5, user)
    review = Review("review here", 4, place, user)
    assert review.text == "review here"
    assert review.rating == 4
    assert review.place == place
    assert review.user == user
    print("Review creation test passed!")

test_review_creation()