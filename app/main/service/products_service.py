from app.main.models.products_model import Products
from ...api.repository import db


class Product():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Products.query.all()

    def post(data):
        product = Products.query.filter_by(
            product=data['product_code']).first()
        if not product:
            new_product = Products(
                product_code=data['product_code'],
                product_name=data['product_name'],
                product_line=data['product_line'],
                product_scale=data['product_scale'],
                product_vendor=data['product_vendor'],
                product_description=data['product_description'],
                quantity_in_stock=data['quantity_in_stock'],
                buy_price=data['buy_price'],
                msrp=data['msrp'],
                )
            Product.save(new_product)
            response_object = {
                'status': 'success',
                'message': 'Product created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Product already exist'
            }
            return response_object, 409

    def put(data):
        product = Products.query.filter_by(product_code=data['product_code']).first()
        if not product:
            response_object = {
                'status': 'fail',
                'message': """Product doesn't exist"""
            }
            return response_object, 409
        else:
            product.product_name=data['product_name']
            product.product_line=data['product_line']
            product.product_scale=data['product_scale']
            product.product_vendor=data['product_vendor']
            product.product_description=data['product_description']
            product.quantity_in_stock=data['quantity_in_stock']
            product.buy_price=data['buy_price']
            product.msrp=data['msrp']
            Product.save(product)
            response_object = {
                'status': 'success',
                'message': 'Product updated'
            }
            return response_object, 201


class PaymentById():
    def delete(product_code):
        product = Products.query.filter_by(product_code=product_code).first()
        if not product:
            response_object = {
                'status': 'fail',
                'message': """Product doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the Product
            Product.delete(product)
            response_object = {
                'status': 'success',
                'message': 'Product deleted'
            }
            return response_object, 201

    def get(product_code):
        return Products.query.filter_by(product_code=product_code).first()
