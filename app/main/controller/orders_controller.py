from flask import request
from flask_restx import Resource

from ...util.dto import OrderDto
from ..service.orders_service import Order, OrderById

api = OrderDto.api
_order = OrderDto.order


@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_registered_order')
    @api.marshal_list_with(_order)
    def get(self):
        return Order.get()

    @api.response(201, 'Order successfully created.')
    @api.doc('create a new order')
    @api.expect(_order, validate=True)
    def post(self):
        data = request.json
        return Order.post(data=data)

    @api.response(201, 'Order successfully updated.')
    @api.doc('update order')
    @api.expect(_order, validate=True)
    def put(self):
        data = request.json
        return Order.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Order identifier')
@api.response(404, 'Order not found.')
class OrderByParam(Resource):
    @api.doc('get an order')
    @api.marshal_with(_order)
    def get(self, public_id):
        id = int(public_id)
        order = OrderById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not order:
            api.abort(404)
        else:
            return order

    def delete(public, public_id):
        id = int(public_id)
        order = OrderById.delete(id)
        return order
