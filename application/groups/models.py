from application import db
from application.models import Base

class Group(Base):
    name = db.Column(db.String(144), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        #t√m√§konstruktori tulee joskus ehk√ saamaan ryhm√n j√senet listana
        self.name = name
