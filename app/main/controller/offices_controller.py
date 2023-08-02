from flask import request
from flask_restx import Resource

from ...util.dto import OfficeDto
from ..service.offices_service import Office, OfficeById

api = OfficeDto.api
_office = OfficeDto.office


@api.route('/')
class OfficeList(Resource):
    @api.doc('list_of_registered_office')
    @api.marshal_list_with(_office, envelope='data')
    def get(self):
        return Office.get()

    @api.response(201, 'Office successfully created.')
    @api.doc('create a new office')
    @api.expect(_office, validate=True)
    def post(self):
        data = request.json
        return Office.post(data=data)

    @api.response(201, 'Office successfully updated.')
    @api.doc('update office')
    @api.expect(_office, validate=True)
    def put(self):
        data = request.json
        return Office.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Office identifier')
@api.response(404, 'Office not found.')
class Office(Resource):
    @api.doc('get a office')
    @api.marshal_with(_office)
    def get(self, public_id):
        id = int(public_id)
        office = OfficeById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not office:
            api.abort(404)
        else:
            return office

    def delete(public, public_id):
        id = int(public_id)
        office = OfficeById.delete(id)
        return office
