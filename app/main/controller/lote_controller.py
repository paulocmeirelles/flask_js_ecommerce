from flask import request
from flask_restx import Resource

from ...util.dto import LoteDto
from ..service.lote_service import Lotes, LoteById

api = LoteDto.api
_lote = LoteDto.lote


@api.route('/')
class LoteList(Resource):
    @api.doc('list_of_registered_lotes')
    @api.marshal_list_with(_lote, envelope='data')
    def get(self):
        return Lotes.get()

    @api.response(201, 'Lote successfully created.')
    @api.doc('create a new lote')
    @api.expect(_lote, validate=True)
    def post(self):
        data = request.json
        return Lotes.post(data=data)

    @api.response(201, 'Lote successfully updated.')
    @api.doc('update lote')
    @api.expect(_lote, validate=True)
    def put(self):
        data = request.json
        return Lotes.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Lote identifier')
@api.response(404, 'Lote not found.')
class Lote(Resource):
    @api.doc('get a lote')
    @api.marshal_with(_lote)
    def get(self, public_id):
        id = int(public_id)
        lote = LoteById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not lote:
            api.abort(404)
        else:
            return lote

    def delete(public, public_id):
        id = int(public_id)
        lote = LoteById.delete(id)
        return lote
