import json
from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from .models import Student, Rooms

api = Blueprint('api', __name__)

@api.route('/api/get_user_name', methods=['POST'])
def get_user_name():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in Student.query.with_entities(Student.name):
            saved_password = Student.query.filter_by(email=email).first().password
            if saved_password == generate_password_hash(password):
                return Student.query.filter_by(email=email).first().name

        return 'Email or Password is invalid'
    return 'Only POST'

@api.route('/api/get_rooms_info', methods=['POST'])
def get_rooms_info():
    print(request.json)
    if request.method == 'POST':
        if 'hostel_id' in request.json and 'gender' in request.json and 'floor' in request.json:
            hostel_id = request.json['hostel_id']
            gender = request.json['gender']
            floor = request.json['floor']

            print(hostel_id, gender, floor)
            out = json.dumps([r.as_dict() for r in Rooms.query.filter_by(hostel_id=hostel_id, gender=gender, floor_num=floor).all()])
            print(out)
            return out

        return 'All fields are required'