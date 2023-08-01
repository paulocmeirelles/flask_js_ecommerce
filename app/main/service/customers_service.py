from app.main.models.customers_model import Customers
from ...api.repository import db


class Customer():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Customers.query.all()

    def post(data):
        customer = Customers.query.filter_by(
            customer_number=data['customer_number']).first()
        if not customer:
            new_customer = Customers(
                customer_name=data['customer_name'],
                contact_last_name=data['contact_last_name'],
                contact_first_name=data['contact_first_name'],
                phone=data['phone'],
                address_line1=data['address_line1'],
                address_line2=data['address_line2'],
                city=data['city'],
                state=data['state'],
                postal_code=data['postal_code'],
                sales_rep_employee_number=data['sales_rep_employee_number'],
                credit_limit=data['credit_limit']
                )
            Customer.save(new_customer)
            response_object = {
                'status': 'success',
                'message': 'Customer created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Customer already exist'
            }
            return response_object, 409

    def put(data):
        customer = Customers.query.filter_by(customer_number=data['customer_number']).first()
        if not customer:
            response_object = {
                'status': 'fail',
                'message': """Customer don't exist"""
            }
            return response_object, 409
        else:
            customer.customer_name=data['customer_name']
            customer.contact_last_name=data['contact_last_name']
            customer.contact_first_name=data['contact_first_name']
            customer.phone=data['phone']
            customer.address_line1=data['address_line1']
            customer.address_line2=data['address_line2']
            customer.city=data['city']
            customer.state=data['state']
            customer.postal_code=data['postal_code']
            customer.sales_rep_employee_number=data['sales_rep_employee_number']
            customer.credit_limit=data['credit_limit']
            Customer.save(customer)
            response_object = {
                'status': 'success',
                'message': 'Customer updated'
            }
            return response_object, 201


class CustomerById():
    def delete(customer_number):
        customer = Customers.query.filter_by(customer_number=customer_number).first()
        if not customer:
            response_object = {
                'status': 'fail',
                'message': """Customers doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the customer
            Customer.delete(customer)
            response_object = {
                'status': 'success',
                'message': 'Customer deleted'
            }
            return response_object, 201

    def get(customer_number):
        return Customers.query.filter_by(customer_number=customer_number).first()
