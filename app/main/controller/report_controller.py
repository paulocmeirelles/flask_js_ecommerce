from flask import make_response
from flask_restx import Resource

from ..helpers import report_helper
from ..service import report_service

from ...util.dto import ReportDto


api = ReportDto.api
_report = ReportDto.report


@api.route('/')
class Report(Resource):
    @api.doc('list_of_registered_boletos')
    # @api.marshal_list_with(_report, envelope='data')
    def get(self):
        table = report_service.Report.get()
        report_helper.dataframe_to_pdf(table, './app/temp/table_report.pdf')
        return make_response(report_helper.read_pdf('./app/temp/table_report.pdf'))
