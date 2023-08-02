from ...api.repository import db
from datetime import datetime


class Orders(db.Model):
    __tablename__ = 'orders'
    order_number = db.Column(db.Integer,primary_key=True, nullable=False)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().strftime('%y-%m-%d'))
    required_date = db.Column(db.Date, nullable=False, default=datetime.now().strftime('%y-%m-%d'))
    shipped_date = db.Column(db.Date, nullable=True, default=None)
    status = db.Column(db.String(15), nullable=False)
    comments = db.Column(db.String(255), nullable=True)
    customer_number = db.Column(db.Integer, nullable=False)