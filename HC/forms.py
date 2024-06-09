from wtforms import StringField, FileField, IntegerField, EmailField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired

# Define a WTForm class for the registration form
class RegistrationForm(FlaskForm):
    # Page 1
    name = StringField('Name', validators=[InputRequired(), ])
    address = StringField('Address', validators=[InputRequired()])
    distance = IntegerField('Distance (KM)', validators=[InputRequired()])
    phone = IntegerField('Mobile Number', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = StringField('Password', validators=[InputRequired()])
    parent_name = StringField("Parent's Name", validators=[InputRequired()])
    parent_phone = IntegerField("Parent's Mobile Number", validators=[InputRequired()])
    # Page 2
    year = SelectField('Year', choices=[('FE','FE'),('SE', 'SE'),('TE', 'TE'),('BE', 'BE')])
    semester = SelectField('Semester', choices=[('1'), ('2')])
    # semester = StringField('Semester', validators=[InputRequired()])
    pr_number = IntegerField('PR Number', validators=[InputRequired()])
    department = SelectField('Department', choices=[('MECH'), ('COMP'), ('ETC'), ('ENE'), ('CIVIL'), ('VLSI'), ('IT')])
    photo = FileField('Upload Photo', validators=[InputRequired()])
    id_proof = FileField('Upload ID Proof', validators=[InputRequired()])

    hostel_num = StringField('Hostel Num')
    room_num = StringField('Room Num') # Manually Done with JS