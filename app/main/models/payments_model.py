from ...api.repository import db
from datetime import datetime


class Payments(db.Model):
    __tablename__ = 'payments'
    customer_number = db.Column(db.Integer, nullable=False)
    check_number = db.Column(db.String(50), primary_key=True,nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%y-%m-%d'))
    amount = db.Column(db.Float(precision=2), nullable=False)