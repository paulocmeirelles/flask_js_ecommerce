from app.main.models.product_lines_model import Product_lines
from ...api.repository import db


class Product_line():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Product_lines.query.all()

    def post(data):
        product_line = Product_lines.query.filter_by(
            product_line=data['product_line']).first()
        if not product_line:
            new_product_line = Product_lines(
                text_description=data['text_description'],
                html_description=data['html_description'],
                image=data['image']
                )
            Product_line.save(new_product_line)
            response_object = {
                'status': 'success',
                'message': 'Product line created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Product line already exist'
            }
            return response_object, 409

    def put(data):
        product_line = Product_lines.query.filter_by(product_line=data['product_line']).first()
        if not product_line:
            response_object = {
                'status': 'fail',
                'message': """Product line doesn't exist"""
            }
            return response_object, 409
        else:
            product_line.text_description=data['text_description']
            product_line.html_description=data['html_description']
            product_line.image=data['image']
            Product_line.save(product_line)
            response_object = {
                'status': 'success',
                'message': 'Product line updated'
            }
            return response_object, 201


class ProductLineById():
    def delete(product_line):
        product_line = Product_lines.query.filter_by(product_line=product_line).first()
        if not product_line:
            response_object = {
                'status': 'fail',
                'message': """Product line doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the Product_line
            Product_line.delete(product_line)
            response_object = {
                'status': 'success',
                'message': 'Product line deleted'
            }
            return response_object, 201

    def get(product_line):
        return Product_lines.query.filter_by(product_line=product_line).first()
