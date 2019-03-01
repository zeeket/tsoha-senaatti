from application import db
from application.models import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Group(Base):
    __tablename__ = 'group'
    name = db.Column(db.String(144), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    group_users = relationship("Group_user", cascade="save-update, merge, delete")

    def __init__(self, name):
        #tämäkonstruktori tulee joskus eä saamaan ryhän äsenet listana
        self.name = name

class GroupAccountLink(Base):
    __tablename__ = 'group_account_link'
    group_id= db.Column(db.Integer, db.ForeignKey('group.id')),
    account_id= db.Column(db.Integer, db.ForeignKey('account.id'))

