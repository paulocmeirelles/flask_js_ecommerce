from app.main.models.payments_model import Payments
from ...api.repository import db


class Payment():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Payments.query.all()

    def post(data):
        payment = Payments.query.filter_by(
            check_number=data['check_number']).first()
        if not payment:
            new_payment = Payments(
                customer_number=data['customer_number'],
                check_number=data['check_number'],
                amount=data['amount']
                )
            Payment.save(new_payment)
            response_object = {
                'status': 'success',
                'message': 'Payment created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Payment already exist'
            }
            return response_object, 409

    def put(data):
        payment = Payments.query.filter_by(check_number=data['check_number']).first()
        if not payment:
            response_object = {
                'status': 'fail',
                'message': """Payment doesn't exist"""
            }
            return response_object, 409
        else:
            payment.customer_number=data['customer_number']
            payment.amount=data['amount']
            payment.payment_date=data['payment_date']
            Payment.save(payment)
            response_object = {
                'status': 'success',
                'message': 'Payment updated'
            }
            return response_object, 201


class PaymentById():
    def delete(check_number):
        payment = Payments.query.filter_by(check_number=check_number).first()
        if not payment:
            response_object = {
                'status': 'fail',
                'message': """Payment doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the Payment
            Payment.delete(payment)
            response_object = {
                'status': 'success',
                'message': 'Payment deleted'
            }
            return response_object, 201

    def get(check_number):
        return Payments.query.filter_by(check_number=check_number).first()
