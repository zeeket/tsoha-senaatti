from application import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    upvotes = db.Column(db.Integer, nullable=False)
    downvotes = db.Column(db.Integer, nullable=False)
    neutralvotes = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.upvotes = 0
        self.downvotes = 0
        self.neutralvotes = 0
        self.done = False
