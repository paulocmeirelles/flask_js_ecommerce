from ...api.repository import db


class Customers(db.Model):
    __tablename__ = 'customers'
    customer_number = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    contact_last_name = db.Column(db.String(50), nullable=False)
    contact_first_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50), nullable=True, default=None)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=True, default=None)
    postal_code = db.Column(db.String(15), nullable=True, default=None)
    country = db.Column(db.String(50), nullable=False)
    sales_rep_employee_number = db.Column(db.Integer, nullable=True)
    credit_limit = db.Column(db.Float(precision=2), nullable=True, default=None)