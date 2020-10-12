from . import db


class Mentor(db.Model):
    __tablename__ = 'MentorDetail'
    UserID = db.Column(db.Integer, primary_key=True)
    Msername = db.Column(db.String(50),
                         index=False,
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(50),
                      index=True,
                      unique=True,
                      nullable=False)
    Github_Url = db.Column(db.String(500),
                           index=True,
                           unique=True,
                           nullable=True)
    linkdln_Url = db.Column(db.String(500),
        index=True,
        unique=True,
        nullable=True)
    Technologies=db.Column(db.String(50),
        index=True,
        unique=True,
        nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.Msername)

