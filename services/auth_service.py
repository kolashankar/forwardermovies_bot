import re
import random
from models import User
from database import get_db

class AuthService:
    def is_valid_phone_number(self, phone_number):
        # Basic phone number validation
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, phone_number) is not None

    def is_valid_email(self, email):
        # Basic email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def authenticate_user(self, telegram_id, phone_number):
        db = next(get_db())
        user = db.query(User).filter(User.telegram_id == telegram_id).first()
        if user:
            user.phone_number = phone_number
            user.is_authenticated = True
        else:
            new_user = User(telegram_id=telegram_id, phone_number=phone_number, is_authenticated=True)
            db.add(new_user)
        db.commit()

    def verify_email(self, telegram_id, email):
        db = next(get_db())
        user = db.query(User).filter(User.telegram_id == telegram_id).first()
        if user:
            user.email = email
            user.is_premium = True
            db.commit()

