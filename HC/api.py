from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Warden, Hostel, Student

api = Blueprint('auth', __name__)

@app.route('/api/get_user_name', methods=['POST'])
def get_user_name():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if saved_password == generate_password_hash(password) and email in Student.querY.with_entities(Student.name):
            return Student.query.filter_by(email=email).first().name 

        return 'Email or Password is invalid'
    return 'Only POST'

