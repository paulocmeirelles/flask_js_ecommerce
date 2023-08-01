from ..service import upload_service
from flask import request
from flask_restx import Resource

from ...util.dto import UploadDto

from ..helpers import upload_helper
api = UploadDto.api


@api.route('/')
class Upload(Resource):

    @api.response(201, 'Upload successfully.')
    @api.doc('upload a new file')
    def post(self):
        data = request.files['file']
        if data.mimetype == 'text/csv':
            json = upload_helper.csv_upload(data.read())
            # verify if data already inputed
            upload_service.Lotes(json)

            return {'status': 'success', 'message': 'csv received'}
        elif data.mimetype == 'application/pdf':
            json = upload_helper.pdf_to_dict(data.read())
            # verify if data already inputed
            upload_service.Boletos(json)
            return {'status': 'success', 'message': 'pdf received'}


# @api.route('/<public_id>')
# @api.param('public_id', 'The Lote identifier')
# @api.response(404, 'Lote not found.')
# class Lote(Resource):
#     @api.doc('get a lote')
#     @api.marshal_with(_lote)
#     def get(self, public_id):
#         id = int(public_id)
#         lote = LoteById.get(id)
#         # return {'message': 'Ok', 'status': 'success'}
#         if not lote:
#             api.abort(404)
#         else:
#             return lote
