from ...api.repository import db
from sqlalchemy import UniqueConstraint
from sqlalchemy.event import listen
    
class Products(db.Model):
    __tablename__ = 'products'
    # product_code = db.Column(db.String(15), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(70), nullable=False)
    product_line = db.Column(db.String(50), nullable=False)
    product_scale = db.Column(db.String(10), nullable=False)
    product_vendor = db.Column(db.String(50), nullable=False)
    product_description = db.Column(db.String(255), nullable=True)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    buy_price = db.Column(db.Float(precision=2), nullable=False)
    msrp = db.Column(db.Float(precision=2), nullable=False)

    __table_args__ = (UniqueConstraint(product_scale,id),)

    @staticmethod
    def product_code(mapper, connection, product):
        product_code = f"""S{product.product_scale.split(':')[1]}_{str(product.id).rjust(5,"0")}"""
        product.product_code = product_code

listen(Products, "before_insert", Products.product_code)