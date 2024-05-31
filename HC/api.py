from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from .models import Student

api = Blueprint('auth', __name__)

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

