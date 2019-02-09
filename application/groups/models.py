from application import db
from application.models import Base

class Group(Base):
    __tablename__ = 'group'
    name = db.Column(db.String(144), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    group_users = relationship("Group_user", cascade="save-update, merge, delete")

    def __init__(self, name):
        #t√m√§konstruktori tulee joskus ehk√ saamaan ryhm√n j√senet listana
        self.name = name

group_accounts = Table('group_accounts', Base.metadata,
                        Column('group_id', Integer, ForeignKey('group.id')),
                        Column('account_id', Integer, ForeignKey('account.id'))
                      )
