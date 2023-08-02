from ...api.repository import db


class Employees(db.Model):
    __tablename__ = 'employees'
    employee_number = db.Column(db.Integer,primary_key=True, nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    extension = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    office_code = db.Column(db.String(10), nullable=False)
    reports_to = db.Column(db.Integer, nullable=True)
    job_Title = db.Column(db.String(50), nullable=False)