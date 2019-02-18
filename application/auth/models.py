from application import db, argon2
from application.models import Base


class User(Base):

    __tablename__ = "account"
    username = db.Column(db.String(144), nullable=False)
    passwordhash = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144))
    polls = db.relationship("Poll", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.passwordhash = argon2.generate_password_hash(password)

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
