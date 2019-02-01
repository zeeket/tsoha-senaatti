from application import db, argon2


class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp()) 

    username = db.Column(db.String(144), nullable=False)
    passwordhash = db.Column(db.String(144), nullable=False)

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
