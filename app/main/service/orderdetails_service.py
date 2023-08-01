from app.main.models.orderdetails_model import OrderDetails
from ...api.repository import db


class OrderDetail():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return OrderDetails.query.all()

    def post(data):
        order_detailed = OrderDetails.query.filter_by(
            order_number=data['order_number']).first()
        if not order_detailed:
            new_order_detailed = OrderDetails(
                product_code=data['product_code'],
                quantity_ordered=data['quantity_ordered'],
                price_each=data['price_each'],
                order_line_number=data['order_line_number']
                )
            OrderDetail.save(new_order_detailed)
            response_object = {
                'status': 'success',
                'message': 'Order detailed created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Order detailed already exist'
            }
            return response_object, 409

    def put(data):
        order_detailed = OrderDetails.query.filter_by(order_number=data['order_number']).first()
        if not order_detailed:
            response_object = {
                'status': 'fail',
                'message': """Order detailed doesn't exist"""
            }
            return response_object, 409
        else:
            order_detailed.product_code=data['product_code']
            order_detailed.quantity_ordered=data['quantity_ordered']
            order_detailed.price_each=data['price_each']
            order_detailed.order_line_number=data['order_line_number']
            OrderDetail.save(order_detailed)
            response_object = {
                'status': 'success',
                'message': 'Order detailed updated'
            }
            return response_object, 201


class OrderDetailsById():
    def delete(order_number):
        order_detailed = OrderDetails.query.filter_by(order_number=order_number).first()
        if not order_detailed:
            response_object = {
                'status': 'fail',
                'message': """Order detailed doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the Order detailed
            OrderDetail.delete(order_detailed)
            response_object = {
                'status': 'success',
                'message': 'Order detailed deleted'
            }
            return response_object, 201

    def get(order_number):
        return OrderDetails.query.filter_by(order_number=order_number).first()
