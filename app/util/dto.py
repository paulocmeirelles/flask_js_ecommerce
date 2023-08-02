from flask_restx import Namespace, fields

class EmployeeDto:
    api = Namespace('employees', description='DTO related to table Employees')
    employee = api.model('employees', {
        'employee_number': fields.Integer(required=True),
        "last_name": fields.Boolean(required=True),
        "first_name": fields.String(required=True),
        "extension": fields.String(required=True),
        "email": fields.String(required=True),
        "office_code": fields.String(required=True),
        "reports_to": fields.Integer(required=False),
        "job_Title": fields.String(required=True),
    })

class OfficeDto:
    api = Namespace('offices', description='DTO related to table Offices')
    office = api.model('offices', {
        'office_code': fields.String(required=True),
        "city": fields.String(required=True),
        "phone": fields.String(required=True),
        "address_line1": fields.String(required=True),
        "address_line2": fields.String(required=False),
        "state": fields.String(required=False),
        "country": fields.String(required=True),
        "postal_code": fields.String(required=True),
        "territory": fields.String(required=True),
    })

class OrderDto:
    api = Namespace('orders', description='DTO related to table Orders')
    order = api.model('orders', {
        'order_number': fields.Integer(required=True),
        "order_date": fields.Date(required=True),
        "required_date": fields.Date(required=True),
        "shipped_date": fields.Date(required=False),
        "status": fields.String(required=True),
        "comments": fields.String(required=False),
        "customer_number": fields.Integer(required=True)
    })

class OrderDetailDto:
    api = Namespace('orderdetails', description='DTO related to table Orders Details')
    order_detail = api.model('orderdetails', {
        'order_number': fields.Integer(required=True),
        "product_code": fields.String(required=True),
        "quantity_ordered": fields.Integer(required=True),
        "price_each": fields.Float(required=True),
        "order_line_number": fields.Integer(required=True)
    })

class PaymentDto:
    api = Namespace('payments', description='DTO related to table Payments')
    payment = api.model('payments', {
        'customer_number': fields.Integer(required=True),
        "check_number": fields.String(required=True, description='this is the primary key'),
        "payment_date": fields.Date(required=True),
        "amount": fields.Float(required=True)
    })


class CustomerDto:
    api = Namespace('customers', description='DTo related to table Customers')
    customer = api.model('customers', {
        'customer_number': fields.Integer(required=True, description='primary key'),
        'customer_name': fields.String(required=True),
        'contact_last_name': fields.String(required=True),
        'contact_first_name': fields.String(required=True),
        'phone': fields.String(required=True),
        "address_line1": fields.String(required=True),
        "address_line2": fields.String(required=False),
        "city": fields.String(required=False),
        "state": fields.String(required=True),
        "postal_code": fields.String(required=True),
        "country": fields.String(required=False),
        "sales_rep_employee_number": fields.Integer(required=True),
        "credit_limit": fields.Float(required=True)
    })

class ProductDto:
    api = Namespace('products', description='DTo related to table Products')
    product = api.model('products', {
        'product_code': fields.String(required=True,description='S(scale)_(id_product)'),
        'product_name': fields.String(required=True),
        'product_line': fields.String(required=True),
        'product_scale': fields.String(required=True),
        'product_vendor': fields.String(required=True),
        "product_description": fields.String(required=False),
        "quantity_in_stock": fields.Integer(required=True),
        "buy_price": fields.Float(required=True),
        "msrp": fields.Float(required=True)
    })

class ProductLineDto:
    api = Namespace('products_lines', description='DTo related to table Product Lines')
    product_line = api.model('products_lines', {
        'product_line': fields.String(required=True),
        'text_description': fields.String(required=False),
        'html_description': fields.String(required=False),
        'image': fields.String(required=False, description='image storaged in bytes'),
    })