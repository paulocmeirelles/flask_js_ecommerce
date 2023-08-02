from flask import request
from flask_restx import Resource

from ...util.dto import ProductDto
from ..service.products_service import Product, ProductById

api = ProductDto.api
_product = ProductDto.product


@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_registered_product')
    @api.marshal_list_with(_product)
    def get(self):
        return Product.get()

    @api.response(201, 'Product successfully created.')
    @api.doc('create a new product')
    @api.expect(_product, validate=True)
    def post(self):
        data = request.json
        return Product.post(data=data)

    @api.response(201, 'Product successfully updated.')
    @api.doc('update product')
    @api.expect(_product, validate=True)
    def put(self):
        data = request.json
        return Product.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Product identifier')
@api.response(404, 'Product not found.')
class ProductByParam(Resource):
    @api.doc('get a product')
    @api.marshal_with(_product)
    def get(self, public_id):
        id = str(public_id).upper()
        product = ProductById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not product:
            api.abort(404)
        else:
            return product

    def delete(public, public_id):
        id = int(public_id)
        product = ProductById.delete(id)
        return product
