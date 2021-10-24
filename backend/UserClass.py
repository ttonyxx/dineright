class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String(10))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)
    profile_pic = db.Column(db.String(128))
    cuisine_preferences = db.Column(db.String(64))
    cuisine_description = db.Column(db.String(64))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'))
    cuisine = db.relationship('Cuisine',
                              backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return '<User {}>'.format(self.username)