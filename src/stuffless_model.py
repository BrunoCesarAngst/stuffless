from peewee import SqliteDatabase, Model, DateTimeField, AutoField, CharField, TextField, Check, ForeignKeyField
from user_model import User
from datetime import datetime
from enum import Enum
from common_model import TimestampedModel, stufflessDB


class ItemState(Enum):
    """
    Enum para os state dos itens
    """
    INBOX = 'inbox'
    DISCERNED = 'discerned'
    FAST_ACTION = 'fastAction'
    INCUBATE = 'incubate'
    REFERENCE = 'reference'
    TRASH = 'trash'
    DELEGATED = 'delegated'
    ACTION_DATE = 'actionDate'
    CONTEXT = 'context'
    PROJECT = 'project'
    COMPLETED = 'completed'


class BaseModel(Model):
    """"
    Modelo base para todos os modelos do banco de dados
    """
    class Meta:
        database = stufflessDB


class StufflessItem(TimestampedModel):
    """
    Modelo para os itens do banco de dados
    """
    id = AutoField(primary_key=True)
    task = CharField()
    description = TextField(null=True)
    state = CharField(constraints=[Check('state in {}'.format(tuple(ItemState.__members__)))])
    user = ForeignKeyField(User, backref='stuffless_items')

    def set_state(self, new_state):
        if new_state == ItemState.INBOX:
            pass
        elif new_state != ItemState.INBOX:
            if self.state == ItemState.INBOX:
                self.state = new_state.value
        else:
            raise ValueError('Invalid state')

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super(StufflessItem, self).save(*args, **kwargs)
