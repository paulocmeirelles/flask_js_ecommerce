from flask_restx import Namespace, fields


class LoteDto:
    api = Namespace('lote', description='lote related operations')
    lote = api.model('lote', {
        'name': fields.String(required=True, description='lote name'),
        "activate": fields.Boolean(required=False, description="lote still activated"),
        "created_at": fields.DateTime(required=False, description="When it was created")
    })


class BoletoDto:
    api = Namespace('boleto', description='boleto related operations')
    boleto = api.model('boleto', {
        'name': fields.String(required=True, description='boleto name'),
        'lote_id': fields.Integer(required=True, description='lote name from table Lote'),
        'month_reference': fields.Integer(required=True, description='month reference of payment'),
        'value': fields.Float(required=False, description='value of boleto'),
        'bar_code': fields.String(required=False, description='bar code of boleto'),
        "activate": fields.Boolean(required=False, description="boleto still activated"),
        "created_at": fields.DateTime(required=False, description="When it was created")
    })


class UploadDto:
    api = Namespace('upload', description='upload of files csv/pdf')


class ReportDto:
    api = Namespace('report', description='report in pdf bytes')
    report = api.model('report', {
        'bytes': fields.String(required=True, description='pandas table to bytes')
    })
