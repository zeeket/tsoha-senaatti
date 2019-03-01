from application import db
from application.models import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from application.auth.models import User

class Poll(Base):

    __tablename__ = "poll"
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(280))
    upvotes = db.Column(db.Integer, nullable=False)
    downvotes = db.Column(db.Integer, nullable=False)
    neutralvotes = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    votes = relationship(User, secondary = 'poll_account_link') 

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


    def get_creator_name(self):
            stmt = text("SELECT account.username FROM account "
                    "WHERE (:pollaccid = account.id)")
            res = db.engine.execute(stmt,pollaccid = self.account_id)
            name = res.first() 
            return name


    def has_voted(self, userid):
        stmt = text("SELECT * FROM poll_account_link "
                "WHERE (poll_account_link.userid = :queryuserid AND poll_account_link.pollid = :querypollid)")
        res = db.engine.execute(stmt,queryuserid=userid,querypollid=self.id)
        if res.fetchone():
            return true
        return false

class Vote(Base):
    __tablename__ = "poll_account_link"
    
    userid = db.Column(db.Integer, db.ForeignKey('account.id'),
            primary_key=True)
    pollid = db.Column(db.Integer, db.ForeignKey('poll.id'),
            primary_key=True)
