from peewee import SqliteDatabase, Model, DateTimeField
from datetime import datetime

# Initialize the database
stufflessDB = SqliteDatabase('stuffless.db')


class TimestampedModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        database = stufflessDB
