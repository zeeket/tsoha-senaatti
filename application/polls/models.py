from application import db
from application.models import Base

class Poll(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(280))
    upvotes = db.Column(db.Integer, nullable=False)
    downvotes = db.Column(db.Integer, nullable=False)
    neutralvotes = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, description):
        self.name = name
        if description is "":
            self.description = "Kuvausta vaille jäänyt, mysteerinomainen senaatti."
        else:
            self.description = description
        self.upvotes = 0
        self.downvotes = 0
        self.neutralvotes = 0
        self.done = False
