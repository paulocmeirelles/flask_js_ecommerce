from app.main.models.offices_model import Offices
from ...api.repository import db


class Office():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def delete(data):
        db.session.delete(data)
        db.session.commit()

    def get():
        return Offices.query.all()

    def post(data):
        office = Offices.query.filter_by(
            office_code=data['employee_code']).first()
        if not office:
            new_office = Offices(
                city=data['city'],
                phone=data['phone'],
                address_line1=data['address_line1'],
                address_line2=data['address_line2'],
                state=data['state'],
                country=data['country'],
                postal_code=data['postal_code'],
                territory=data['territory'],
                )
            Office.save(new_office)
            response_object = {
                'status': 'success',
                'message': 'Office created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Office already exist'
            }
            return response_object, 409

    def put(data):
        office = Offices.query.filter_by(office_code=data['office_code']).first()
        if not office:
            response_object = {
                'status': 'fail',
                'message': """Employee doesn't exist"""
            }
            return response_object, 409
        else:
            office.city=data['city']
            office.phone=data['phone']
            office.address_line1=data['address_line1']
            office.address_line2=data['address_line2']
            office.state=data['state']
            office.country=data['country']
            office.postal_code=data['postal_code']
            office.territory=data['territory']
            Office.save(office)
            response_object = {
                'status': 'success',
                'message': 'Office updated'
            }
            return response_object, 201


class OfficeById():
    def delete(office_code):
        office = Offices.query.filter_by(office_code=office_code).first()
        if not office:
            response_object = {
                'status': 'fail',
                'message': """Office doesn't exist""" 
            }
            return response_object, 409
        else:
            # The best thing here is deactivate the office
            Office.delete(office)
            response_object = {
                'status': 'success',
                'message': 'Office deleted'
            }
            return response_object, 201

    def get(office_code):
        return Offices.query.filter_by(office_code=office_code).first()
