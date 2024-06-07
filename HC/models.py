from . import db
from flask_login import UserMixin

class Warden(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Warden {self.id} {self.email} {self.password} {self.name}"

class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    warden_id = db.Column(db.Integer, nullable=False)
    hostel_id = db.Column(db.Integer, nullable=False)
    floor_num = db.Column(db.Integer, nullable=False)
    nrooms = db.Column(db.Integer, nullable=False)
    noccupied_rooms = db.Column(db.Integer, nullable=False)
    nstudents = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Hostel {self.id} {self.warden_id} {self.hostel_id} {self.nrooms} {self.noccupied_rooms} {self.nstudents}"
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_approved = db.Column(db.Boolean, nullable=False, default=False)
    warden_id = db.Column(db.Integer, nullable=False)
    hostel_id = db.Column(db.Integer, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    room_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    parent_name = db.Column(db.String(100), nullable=False)
    parent_phone = db.Column(db.String(10), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    semester = db.Column(db.String(100), nullable=False)
    pr_number = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100), nullable=True)
    id_proof = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f'''Student {self.id} {self.warden_id} {self.is_approved} {self.hostel_id} {self.room_num} {self.name} {self.address}{self.phone} {self.email}
                            {self.parent_name} {self.parent_phone} {self.year} {self.semester} {self.pr_number} {self.department} {self.photo} {self.id_proof}'''
