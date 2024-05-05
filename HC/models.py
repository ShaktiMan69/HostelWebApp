from . import db

class Warden(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)

class HostelInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalhostels = db.Column(db.Integer, nullable=False)
    boyshostels = db.Column(db.Integer, nullable=False)
    girlshostels = db.Column(db.Integer, nullable=False)
    totalstudents = db.Column(db.Integer, nullable=False)
    totalboys = db.Column(db.Integer, nullable=False)
    totalgirls = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'HostelInfo' + str(self.id)


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hname = db.Column(db.String(30), nullable=False)
    warden = db.Column(db.String(30), nullable=False)
    nrooms = db.Column(db.Integer, nullable=False)
    noccupied_rooms = db.Column(db.Integer, nullable=False)
    nstudents = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Integer, nullable=False)
    messfee = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Hostel' + str(self.id)