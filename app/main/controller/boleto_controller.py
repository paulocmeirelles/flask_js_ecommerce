from flask import request
from flask_restx import Resource

from ...util.dto import BoletoDto
from ..service.boleto_service import Boletos, BoletoById

api = BoletoDto.api
_boleto = BoletoDto.boleto


@api.route('/')
class BoletoList(Resource):
    @api.doc('list_of_registered_boletos')
    @api.marshal_list_with(_boleto, envelope='data')
    def get(self):
        return Boletos.get()

    @api.response(201, 'Boleto successfully created.')
    @api.doc('create a new boleto')
    @api.expect(_boleto, validate=True)
    def post(self):
        data = request.json
        return Boletos.post(data=data)

    @api.response(201, 'Boleto successfully updated.')
    @api.doc('update boleto')
    @api.expect(_boleto, validate=True)
    def put(self):
        data = request.json
        return Boletos.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Boleto identifier')
@api.response(404, 'Boleto not found.')
class Boleto(Resource):
    @api.doc('get a boleto')
    @api.marshal_with(_boleto)
    def get(self, public_id):
        id = int(public_id)
        boleto = BoletoById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not boleto:
            api.abort(404)
        else:
            return boleto

    def delete(public, public_id):
        id = int(public_id)
        boleto = BoletoById.delete(id)
        return boleto
