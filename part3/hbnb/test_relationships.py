from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

app = create_app()

with app.app_context():
    # Reset database
    db.drop_all()
    db.create_all()

    # Create a user
    user = User(
        first_name="Arveen",
        last_name="Mogun",
        email="arveen@test.com"
    )
    user.hash_password("1234")
    db.session.add(user)
    db.session.commit()
    print("User:", user.id, user.email)

    # Create a place for the user
    place = Place(
        title="My Cozy Place",
        description="Nice and cozy",
        price=100.0,
        latitude=10.0,
        longitude=20.0,
        user_id=user.id
    )
    db.session.add(place)
    db.session.commit()
    print("Place:", place.id, place.title, "Owner:", place.owner.first_name)

    # Create a review for the place by the user
    review = Review(
        text="Great stay!",
        rating=5,
        user_id=user.id,
        place_id=place.id
    )
    db.session.add(review)
    db.session.commit()
    print("Review:", review.id, review.text, "Author:", review.author.first_name, "Place:", review.place.title)

    # Create an amenity and link to place
    amenity = Amenity(name="Wi-Fi")
    db.session.add(amenity)
    db.session.commit()
    place.amenities.append(amenity)
    db.session.commit()
    print("Amenity:", amenity.id, amenity.name, "Places linked:", [p.title for p in amenity.places])