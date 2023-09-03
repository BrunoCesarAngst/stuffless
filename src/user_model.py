from peewee import Model, CharField, DateTimeField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from common_model import TimestampedModel, stufflessDB


class User(TimestampedModel):
    username = CharField(unique=True)
    _hashed_password = CharField(max_length=255)

    @property
    def password(self):
        return self._hashed_password

    @password.setter
    def password(self, value):
        self._hashed_password = generate_password_hash(value)

    def verify_password(self, value):
        return check_password_hash(self._hashed_password, value)

    class Meta:
        database = stufflessDB
