from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Warden, Hostel, Student

auth = Blueprint('auth', __name__)

# TODO 
@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # code to validate and add user to database goes here
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = Warden.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('auth.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = Warden(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # login code goes here
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = Warden.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('auth.admin'))
    
    return render_template('login.html', page_name='LogIn')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@login_required
@auth.route('/admin')
def admin():
    if current_user.is_authenticated:
        hostel_details = Hostel.query.where(Hostel.warden_id == current_user.id).first() # only show the assigned hostel details to the assigned warden
        students = Student.query.where(Student.warden_id == current_user.id).all()
            
        return render_template("dashboard.html", students=students, hostel=hostel_details, current_user = current_user.name)
    
    return redirect(url_for('auth.login'))


@login_required
@auth.route('/students')
def hostel():
    if current_user.is_authenticated:
        students = Student.query.all()
        return render_template('stdlist.html', students=students, current_user=current_user.name)
    
    return redirect(url_for('auth.login'))

@login_required
@auth.route('/student/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if current_user.is_authenticated:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return redirect('/students')
    return redirect(url_for('auth.login'))
    
@login_required
@auth.route('/student/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    if current_user.is_authenticated:
        info = Student.query.get_or_404(id)
        if request.method == 'POST':
            info.warden_id = request.form['warden_id']
            info.hostel_id = request.form['hostel_id']
            info.password = request.form['password']
            info.room_num = request.form['room_num']
            info.name = request.form['name']
            info.address = request.form['address']
            info.phone = request.form['phone']
            info.email = request.form['email']
            info.parent_name = request.form['parent_name']
            info.parent_phone = request.form['parent_phone']
            info.year = request.form['year']
            info.semester = request.form['semester']
            info.pr_number = request.form['pr_number']
            info.department = request.form['department']
            db.session.commit()
            return redirect('/students')
        else:
            return render_template('edit-student.html', info=info, current_user=current_user.name)
        
    return redirect(url_for('auth.login'))