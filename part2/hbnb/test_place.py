from app.models.place import Place
from app.models.user import User

def test_place_creation():
    user = User("John", "Doe", "a@b.c")
    place = Place("house", "it's a house", 100, 50.0, -100.5, user)
    assert place.title == "house"
    assert place.description == "it's a house"
    assert place.price == 100
    assert place.latitude == 50.0
    assert place.longitude == -100.5
    assert place.owner.first_name == user.first_name
    assert place.owner.last_name == user.last_name
    assert place.owner.email == user.email
    print("Place creation test passed!")

test_place_creation()