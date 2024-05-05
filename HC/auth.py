from flask import Blueprint, request, render_template, url_for, redirect
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .main import HostelInfo, Hostel
from .models import Warden

auth = Blueprint('auth', __name__)

@auth.route('/rooms')
def rooms():
    return 'Rooms'

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

@auth.route('/logout')
def logout():
    return 'Logout'
    
@auth.route('/admin')
def admin():
    info = HostelInfo.query.get(1)
    hostel_names = Hostel.query.with_entities(Hostel.hname).all()

    current_hostel = request.args.get('hostel')
    if current_hostel:
        hostel = Hostel.query.where(Hostel.hname == current_hostel).first()
        return render_template("dashboard.html", info=info, hostel_names = hostel_names, current_hostel = current_hostel, hostel=hostel)
        
    return render_template("dashboard.html", info=info, hostel_names = hostel_names, current_hostel = "Select a Hostel")

@auth.route('/hostels')
def hostel():
    hostels = Hostel.query.all()
    return render_template('hostels.html', hostels=hostels)

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

@auth.route('/add-hostel', methods=['GET', 'POST'])
def addhostel():
    if request.method == 'POST':
        info = HostelInfo.query.get(1)
        info.totalhostels = info.totalhostels + 1
        info.boyshostels = info.boyshostels + 1
        hname = request.form['hname']
        warden = request.form['warden']
        nrooms = request.form['nrooms']
        nstudents = request.form['nstudents']
        info.totalstudents += int(nstudents)
        fee = request.form['fee']
        messfee = request.form['messfee']
        new_hostel = Hostel(hname=hname, warden=warden, nrooms=nrooms,
                            nstudents=nstudents, fee=fee, messfee=messfee)
        db.session.add(new_hostel)
        db.session.commit()
        return redirect('/admin')
    else:
        return render_template('addhostel.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        info = HostelInfo.query.get(1)
        info.totalhostels = info.totalhostels + 1
        info.boyshostels = info.boyshostels + 1
        hname = request.form['hname']
        warden = request.form['warden']
        nrooms = request.form['nrooms']
        nstudents = request.form['nstudents']
        info.totalstudents += int(nstudents)
        fee = request.form['fee']
        messfee = request.form['messfee']
        new_hostel = Hostel(hname=hname, warden=warden, nrooms=nrooms,
                            nstudents=nstudents, fee=fee, messfee=messfee)
        db.session.add(new_hostel)
        db.session.commit()
        return redirect('/admin')
    else:
        return render_template('register.html')
    
@auth.route('/hostels/edit/<int:id>', methods=['GET', 'POST'])
def update(id):
    info = Hostel.query.get_or_404(id)
    if request.method == 'POST':
        info2 = HostelInfo.query.get(1)
        info2.totalstudents -= int(info.nstudents)
        info.hname = request.form['hname']
        info.warden = request.form['warden']
        info.nrooms = request.form['nrooms']
        info.nstudents = request.form['nstudents']
        info.fee = request.form['fee']
        info.messfee = request.form['messfee']
        info2.totalstudents += int(info.nstudents)
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
        return render_template('edit.html', info=info)
