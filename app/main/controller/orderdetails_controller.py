from flask import request
from flask_restx import Resource

from ...util.dto import OrderDetailDto
from ..service.orderdetails_service import OrderDetail, OrderDetailsById

api = OrderDetailDto.api
_orderdetail = OrderDetailDto.order_detail


@api.route('/')
class OrderDetailList(Resource):
    @api.doc('list_of_registered_orderdetail')
    @api.marshal_list_with(_orderdetail)
    def get(self):
        return OrderDetail.get()

    @api.response(201, 'OrderDetail successfully created.')
    @api.doc('create a new orderdetail')
    @api.expect(_orderdetail, validate=True)
    def post(self):
        data = request.json
        return OrderDetail.post(data=data)

    @api.response(201, 'OrderDetail successfully updated.')
    @api.doc('update orderdetail')
    @api.expect(_orderdetail, validate=True)
    def put(self):
        data = request.json
        return OrderDetail.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The OrderDetail identifier')
@api.response(404, 'OrderDetail not found.')
class OrderDetailByParam(Resource):
    @api.doc('get an orderdetail')
    @api.marshal_with(_orderdetail)
    def get(self, public_id):
        id = int(public_id)
        orderdetail = OrderDetailsById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not orderdetail:
            api.abort(404)
        else:
            return orderdetail

    def delete(public, public_id):
        id = int(public_id)
        orderdetail = OrderDetailsById.delete(id)
        return orderdetail
