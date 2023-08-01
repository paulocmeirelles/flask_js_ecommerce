from app.main.models.employees_model import Employees
from ...api.repository import db


class Employee():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Employees.query.all()

    def post(data):
        employee = Employees.query.filter_by(
            employee_number=data['employee_number']).first()
        if not employee:
            new_employee = Employees(
                last_name=data['last_name'],
                first_name=data['first_name'],
                extension=data['extension'],
                email=data['email'],
                office_code=data['office_code'],
                reports_to=data['reports_to'],
                job_Title=data['job_Title']
                )
            Employee.save(new_employee)
            response_object = {
                'status': 'success',
                'message': 'Employee created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Employee already exist'
            }
            return response_object, 409

    def put(data):
        employee = Employees.query.filter_by(employee_number=data['employee_number']).first()
        if not employee:
            response_object = {
                'status': 'fail',
                'message': """Employee doesn't exist"""
            }
            return response_object, 409
        else:
            employee.last_name=data['last_name']
            employee.first_name=data['first_name']
            employee.extension=data['extension']
            employee.email=data['email']
            employee.office_code=data['office_code']
            employee.reports_to=data['reports_to']
            employee.job_Title=data['job_Title']
            Employee.save(employee)
            response_object = {
                'status': 'success',
                'message': 'Employee updated'
            }
            return response_object, 201


class EmployeeById():
    def delete(employee_number):
        employee = Employees.query.filter_by(employee_number=employee_number).first()
        if not employee:
            response_object = {
                'status': 'fail',
                'message': """Employee doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the employee
            Employee.delete(employee)
            response_object = {
                'status': 'success',
                'message': 'Employee deleted'
            }
            return response_object, 201

    def get(employee_number):
        return Employees.query.filter_by(employee_number=employee_number).first()
