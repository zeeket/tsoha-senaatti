from application import db, argon2
from application.models import Base
from sqlalchemy.orm import relationship
 
class User(Base):

    __tablename__ = "account"
    username = db.Column(db.String(144), nullable=False)
    passwordhash = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)
    polls = db.relationship("Poll", backref='account', lazy=True)
    groups = relationship('Group', secondary = 'group_account_link')
    votes = relationship("Poll", secondary = 'poll_account_link')

    def __init__(self, username, password):
        self.username = username
        self.passwordhash = argon2.generate_password_hash(password)
        self.role = 'User'

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return this.role
