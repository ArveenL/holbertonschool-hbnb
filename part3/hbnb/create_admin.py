# create_admin.py
from app import create_app
from app.models.user import User
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():
    from app import storage  # import storage after app context is created

    # Check if admin exists
    users = storage.all(User)
    for u in users.values():
        if u.email == "admin@hbnb.io":
            print("Admin already exists!")
            exit(0)

    hashed_pw = bcrypt.generate_password_hash("Admin1234").decode("utf-8")

    admin = User(
        first_name="Admin",
        last_name="User",
        email="admin@hbnb.io",
        password=hashed_pw
    )

    storage.new(admin)
    storage.save()
    print("Admin user created successfully!")