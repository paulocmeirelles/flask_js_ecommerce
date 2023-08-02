from ...api.repository import db


class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    order_number = db.Column(db.Integer, primary_key=True,nullable=False)
    product_code = db.Column(db.String(15), nullable=False)
    quantity_ordered = db.Column(db.Integer, nullable=False)
    price_each = db.Column(db.Float(precision=2), nullable=False)
    order_line_number = db.Column(db.Integer, nullable=False)