from ...api.repository import db


class Offices(db.Model):
    __tablename__ = 'offices'
    office_code = db.Column(db.String(10),primary_key=True, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50), nullable=True, default=None)
    state = db.Column(db.String(50), nullable=True, default=None)
    country = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(15), nullable=False)
    territory = db.Column(db.String(10), nullable=False)