from app.main.models.orders_model import Orders
from ...api.repository import db


class Order():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Orders.query.all()

    def post(data):
        order = Orders.query.filter_by(
            order_number=data['order_number']).first()
        if not order:
            new_order = Orders(
                required_date=data['required_date'],
                shipped_date=data['shipped_date'],
                status=data['status'],
                comments=data['comments'],
                customer_number=data['customer_number']
                )
            Order.save(new_order)
            response_object = {
                'status': 'success',
                'message': 'Order created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Order already exist'
            }
            return response_object, 409

    def put(data):
        order = Orders.query.filter_by(order_number=data['order_number']).first()
        if not order:
            response_object = {
                'status': 'fail',
                'message': """Order doesn't exist"""
            }
            return response_object, 409
        else:
            order.required_date=data['required_date']
            order.shipped_date=data['shipped_date']
            order.status=data['status']
            order.comments=data['comments']
            order.customer_number=data['customer_number']
            Order.save(order)
            response_object = {
                'status': 'success',
                'message': 'Order updated'
            }
            return response_object, 201


class OrderById():
    def delete(order_number):
        order = Orders.query.filter_by(order_number=order_number).first()
        if not order:
            response_object = {
                'status': 'fail',
                'message': """Order doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the Order
            Order.delete(order)
            response_object = {
                'status': 'success',
                'message': 'Order deleted'
            }
            return response_object, 201

    def get(order_number):
        return Orders.query.filter_by(order_number=order_number).first()
