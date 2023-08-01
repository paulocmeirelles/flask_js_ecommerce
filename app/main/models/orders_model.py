from ...api.repository import db
from datetime import datetime


class Orders(db.Model):
    __tablename__ = 'orders'
    order_number = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now().strptime('%y-%m-%d'))
    required_date = db.Column(db.DateTime, nullable=False, default=datetime.now().strptime('%y-%m-%d'))
    shipped_date = db.Column(db.Float(precision=2), nullable=True, default=None)
    status = db.Column(db.String(15), nullable=False)
    comments = db.Column(db.String(255), nullable=True)
    customer_number = db.Column(db.Integer, nullable=False)