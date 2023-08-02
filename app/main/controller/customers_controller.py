from flask import request
from flask_restx import Resource

from ...util.dto import CustomerDto
from ..service.customers_service import Customer, CustomerById

api = CustomerDto.api
_customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customer')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        return Customer.get()

    @api.response(201, 'Customer successfully created.')
    @api.doc('create a new customer')
    @api.expect(_customer, validate=True)
    def post(self):
        data = request.json
        return Customer.post(data=data)

    @api.response(201, 'Customer successfully updated.')
    @api.doc('update customer')
    @api.expect(_customer, validate=True)
    def put(self):
        data = request.json
        return Customer.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Customer identifier')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, public_id):
        id = int(public_id)
        customer = CustomerById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not customer:
            api.abort(404)
        else:
            return customer

    def delete(public, public_id):
        id = int(public_id)
        customer = CustomerById.delete(id)
        return customer
