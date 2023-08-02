from flask import request
from flask_restx import Resource

from ...util.dto import EmployeeDto
from ..service.employees_service import Employee, EmployeeById

api = EmployeeDto.api
_employee = EmployeeDto.employee


@api.route('/')
class EmployeeList(Resource):
    @api.doc('list_of_registered_employee')
    @api.marshal_list_with(_employee, envelope='data')
    def get(self):
        return Employee.get()

    @api.response(201, 'Employee successfully created.')
    @api.doc('create a new employee')
    @api.expect(_employee, validate=True)
    def post(self):
        data = request.json
        return Employee.post(data=data)

    @api.response(201, 'Employee successfully updated.')
    @api.doc('update employee')
    @api.expect(_employee, validate=True)
    def put(self):
        data = request.json
        return Employee.put(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Employee identifier')
@api.response(404, 'Employee not found.')
class Employee(Resource):
    @api.doc('get a employee')
    @api.marshal_with(_employee)
    def get(self, public_id):
        id = int(public_id)
        employee = EmployeeById.get(id)
        # return {'message': 'Ok', 'status': 'success'}
        if not employee:
            api.abort(404)
        else:
            return employee

    def delete(public, public_id):
        id = int(public_id)
        employee = EmployeeById.delete(id)
        return employee
