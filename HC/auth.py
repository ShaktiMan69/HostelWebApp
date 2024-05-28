from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
<<<<<<< HEAD
from .models import Warden, Hostel, Student

auth = Blueprint('auth', __name__)

# TODO 
=======
from .models import Warden, HostelInfo, Hostel

auth = Blueprint('auth', __name__)

# TODO Adibaba told not to do this
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
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
<<<<<<< HEAD
        print(user, user.password, password)
=======
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('auth.admin'))
    
    return render_template('login.html', page_name='LogIn')

@auth.route('/logout')
@login_required
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@login_required
<<<<<<< HEAD
@auth.route('/admin')
def admin():
    if current_user.is_authenticated:
        hostel_details = Hostel.query.where(Hostel.warden_id == current_user.id).first() # only show the assigned hostel details to the assigned warden
        students = Student.query.where(Student.warden_id == current_user.id).all()
            
        return render_template("dashboard.html", students=students, hostel=hostel_details, current_hostel = "Select a Hostel", current_user = current_user.name)
=======
@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_authenticated:
        info = HostelInfo.query.get(1)
        hostel_names = Hostel.query.with_entities(Hostel.hname).all()

        current_hostel = request.args.get('hostel')
        if current_hostel:
            hostel = Hostel.query.where(Hostel.hname == current_hostel).first()
            return render_template("dashboard.html", info=info, hostel_names = hostel_names, current_hostel = current_hostel, hostel=hostel, current_user = current_user.name)
            
        return render_template("dashboard.html", info=info, hostel_names = hostel_names, current_hostel = "Select a Hostel", current_user = current_user.name)
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
    
    return redirect(url_for('auth.login'))


@auth.route('/hostels')
def hostel():
    hostels = Hostel.query.all()
    return render_template('hostels.html', hostels=hostels, current_user = current_user.name)
    return render_template('hostels.html', hostels=hostels, current_user = current_user.name)

@auth.route('/hostel-info/<int:id>',methods=['GET'])
def abc(id):
    info=Hostel.query.get(id)
    return render_template("k.html",info=info)

@auth.route('/hostels/delete/<int:id>', methods=['GET', 'POSTS'])
def delete(id):
    hostel = Hostel.query.get_or_404(id)
    info = HostelInfo.query.get(1)
    info.totalhostels = info.totalhostels - 1
    info.boyshostels = info.boyshostels - 1
    info.totalstudents -= int(hostel.nstudents)
    db.session.delete(hostel)
    db.session.commit()
    return redirect('/hostels')


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         info = HostelInfo.query.get(1)
#         info.totalhostels = info.totalhostels + 1
#         info.boyshostels = info.boyshostels + 1
#         hname = request.form['hname']
#         warden = request.form['warden']
#         nrooms = request.form['nrooms']
#         nstudents = request.form['nstudents']
#         info.totalstudents += int(nstudents)
#         fee = request.form['fee']
#         messfee = request.form['messfee']
#         new_hostel = Hostel(hname=hname, warden=warden, nrooms=nrooms,
#                             nstudents=nstudents, fee=fee, messfee=messfee)
#         db.session.add(new_hostel)
#         db.session.commit()
#         return redirect('/admin')
#     else:
#         return render_template('register.html')

# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         info = HostelInfo.query.get(1)
#         info.totalhostels = info.totalhostels + 1
#         info.boyshostels = info.boyshostels + 1
#         hname = request.form['hname']
#         warden = request.form['warden']
#         nrooms = request.form['nrooms']
#         nstudents = request.form['nstudents']
#         info.totalstudents += int(nstudents)
#         fee = request.form['fee']
#         messfee = request.form['messfee']
#         new_hostel = Hostel(hname=hname, warden=warden, nrooms=nrooms,
#                             nstudents=nstudents, fee=fee, messfee=messfee)
#         db.session.add(new_hostel)
#         db.session.commit()
#         return redirect('/admin')
#     else:
#         return render_template('register.html')
    
@auth.route('/hostels/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    info = Hostel.query.get_or_404(id)
    if request.method == 'POST':
        info.hname = request.form['hname']
        info.warden = request.form['warden']
        info.nrooms = request.form['nrooms']
        info.nstudents = request.form['nstudents']
        info.fee = request.form['fee']
        info.messfee = request.form['messfee']
        db.session.commit()
        return redirect('/hostels')
    else:
        return render_template('edit-hostel.html', info=info)

@auth.route('/edit-info', methods=['GET', 'POST'])
def edit():
    info = HostelInfo.query.get_or_404(1)
    if request.method == 'POST':
        info.totalhostels = request.form['totalhostels']
        info.boyshostels = request.form['boyshostels']
        info.girlshostels = request.form['girlshostels']
        info.totalstudents = request.form['totalstudents']
        info.totalboys = request.form['totalboys']
        info.totalgirls = request.form['totalgirls']
        db.session.commit()
        return redirect('/admin')
    else:
        return render_template('edit.html', info=info, current_user=current_user.name)
        return render_template('edit.html', info=info, current_user=current_user.name)
