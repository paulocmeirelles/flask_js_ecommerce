from flask_restx import Api
from flask import Blueprint

from ..main.controller.lote_controller import api as lote_ns
from ..main.controller.boleto_controller import api as boleto_ns
from ..main.controller.upload_controller import api as upload_ns
from ..main.controller.report_controller import api as report_ns

api_bp = Blueprint('api', __name__)

api = Api(api_bp,
          title='FLASK',
          version='1.0',
          description='Using flask to create an API'
          )

api.add_namespace(lote_ns, path='/lote')
api.add_namespace(boleto_ns, path='/boleto')
api.add_namespace(upload_ns, path='/file')
api.add_namespace(report_ns, path='/report')
