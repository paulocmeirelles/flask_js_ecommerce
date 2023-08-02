from flask import request
from flask_restx import Resource

from ...util.dto import PaymentDto
from ..service.payments_service import Payment, PaymentById

api = PaymentDto.api
_payment = PaymentDto.payment


@api.route('/')
class PaymentList(Resource):
    @api.doc('list_of_registered_payment')
    @api.marshal_list_with(_payment)
    def get(self):
        return Payment.get()

    @api.response(201, 'Payment successfully created.')
    @api.doc('create a new payment')
    @api.expect(_payment, validate=True)
    def post(self):
        data = request.json
        return Payment.post(data=data)

    @api.response(201, 'Payment successfully updated.')
    @api.doc('update payment')
    @api.expect(_payment, validate=True)
    def put(self):
        data = request.json
        return Payment.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Payment identifier')
@api.response(404, 'Payment not found.')
class PaymentByParam(Resource):
    @api.doc('get a payment')
    @api.marshal_with(_payment)
    def get(self, public_id):
        id = str(public_id)
        payment = PaymentById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not payment:
            api.abort(404)
        else:
            return payment

    def delete(public, public_id):
        id = int(public_id)
        payment = PaymentById.delete(id)
        return payment
