from Rezerv import db

class Statuses(db.Model):
    __tablename__ = "Statuses"
    ID  = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String)
