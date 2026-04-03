from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.services.facade import facade

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = facade.create_user({
        "first_name": "Arveen",
        "last_name": "Mogun",
        "email": "arveen@test.com",
        "password": "1234"
    })
    print("User:", user.id, user.email)

    place = facade.create_place({
        "title": "My Place",
        "description": "Nice place",
        "price": 100,
        "latitude": 10.0,
        "longitude": 20.0,
        "user_id": user.id
    })
    print("Place:", place.id, place.title)

    review = facade.create_review({
        "text": "Great stay!",
        "rating": 5,
        "user_id": user.id,
        "place_id": place.id
    })
    print("Review:", review.id, review.text)

    amenity = facade.create_amenity({"name": "Wi-Fi"})
    print("Amenity:", amenity.id, amenity.name)