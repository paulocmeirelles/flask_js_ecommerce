from flask import request
from flask_restx import Resource

from ...util.dto import ProductLineDto
from ..service.product_lines_service import Product_line, ProductLineById

api = ProductLineDto.api
_product_line = ProductLineDto.product_line


@api.route('/')
class Product_lineList(Resource):
    @api.doc('list_of_registered_product_line')
    @api.marshal_list_with(_product_line, envelope='data')
    def get(self):
        return Product_line.get()

    @api.response(201, 'Product_line successfully created.')
    @api.doc('create a new product_line')
    @api.expect(_product_line, validate=True)
    def post(self):
        data = request.json
        return Product_line.post(data=data)

    @api.response(201, 'Product_line successfully updated.')
    @api.doc('update product_line')
    @api.expect(_product_line, validate=True)
    def put(self):
        data = request.json
        return Product_line.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Product_line identifier')
@api.response(404, 'Product_line not found.')
class Product_line(Resource):
    @api.doc('get a product_line')
    @api.marshal_with(_product_line)
    def get(self, public_id):
        id = int(public_id)
        product_line = ProductLineById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not product_line:
            api.abort(404)
        else:
            return product_line

    def delete(public, public_id):
        id = int(public_id)
        product_line = ProductLineById.delete(id)
        return product_line
