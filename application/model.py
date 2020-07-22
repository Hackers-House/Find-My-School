from . import db
class User(db.Model):
    __tablename__='UserDetail'
    UserID=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),
        index=False,
        unique=True,
        nullable=False)
    email=db.Column(db.String(50),
        index=True,
        unique=True,
        nullable=False)
    Github_Url=db.Column(db.String(500),
        index=True,
        unique=True,
        nullable=True)
    linkdln_Url=db.Column(db.String(500),
        index=True,
        unique=True,
        nullable=True)
    Technologies=db.Column(db.String(50),
        index=True,
        unique=True,
        nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.username)