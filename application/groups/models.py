from application import db
from application.models import Base
from application.auth.models import User
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Group(Base):
    __tablename__ = 'group'
    name = db.Column(db.String(144), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    group_accounts = relationship(User, secondary = 'group_account_link')

    def __init__(self, members):
        for m in members:
            try:
                self.group_accounts.append(m)
            except:
                pass 

class GroupAccountLink(Base):
    __tablename__ = 'group_account_link'
    group_id= db.Column(db.Integer, db.ForeignKey('group.id'))
    account_id= db.Column(db.Integer, db.ForeignKey('account.id'))

