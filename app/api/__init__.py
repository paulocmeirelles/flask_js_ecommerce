from flask_restx import Api
from flask import Blueprint

from ..main.controller.customers_controller import api as customers_endpoint
from ..main.controller.employees_controller import api as employees_endpoint
from ..main.controller.offices_controller import api as offices_endpoint
from ..main.controller.orderdetails_controller import api as orderdetails_endpoint
from ..main.controller.orders_controller import api as orders_endpoint
from ..main.controller.payments_controller import api as payments_endpoint
from ..main.controller.product_lines_controller import api as product_lines_endpoint
from ..main.controller.products_controller import api as products_endpoint

api_bp = Blueprint('api', __name__)

api = Api(api_bp,
          title='FLASK',
          version='1.0',
          description='Using flask to create an API'
          )

api.add_namespace(customers_endpoint, path='/customers')
api.add_namespace(employees_endpoint, path='/employees')
api.add_namespace(offices_endpoint, path='/offices')
api.add_namespace(orderdetails_endpoint, path='/orderdetails')
api.add_namespace(orders_endpoint, path='/orders')
api.add_namespace(payments_endpoint, path='/payments')
api.add_namespace(product_lines_endpoint, path='/productlines')
api.add_namespace(products_endpoint, path='/products')
