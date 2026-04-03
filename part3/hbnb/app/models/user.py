from app import db, bcrypt
from app.models.baseModel import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    # User attributes
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

   
    # PASSWORD METHODS (hashes a plain-text password using Flask-Bcrypt 
    # and stores it as a string in the database. 
    # Ensures that passwords are secure and can later be verified without ever storing the raw password.)
    def hash_password(self, password):
        """Hash the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)