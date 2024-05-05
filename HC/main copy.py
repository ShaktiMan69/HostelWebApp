from flask import Flask, render_template, request, redirect, Blueprint
from . import db
from .models import Hostel, HostelInfo

# Reset Database
# with app.app_context():
#     db.drop_all()
#     db.create_all()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    hostels = Hostel.query.all()
    return render_template("index.html", hostels=hostels)