from database import SessionLocal
from models import User
from auth import create_access_token
import bcrypt

class UserHelper:

    def __init__(self):
        self.db = SessionLocal()

    def signup(self, username, email, password):

        existing = self.db.query(User).filter(
            User.username == username
        ).first()

        if existing:
            return {"message": "User already exists"}

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        self.db.add(user)
        self.db.commit()

        return {"message": "Signup successful"}

    def login(self, username, password):

        user = self.db.query(User).filter(
            User.username == username
        ).first()

        if not user:
            return {"message": "User not found"}

        if not bcrypt.checkpw(
            password.encode(),
            user.password.encode()
        ):
            return {"message": "Wrong password"}
        access_token = create_access_token(user.id)

        return {
            "message": "Login successful",
            "acess_token": access_token
        }