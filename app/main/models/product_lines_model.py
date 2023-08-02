from ...api.repository import db
from sqlalchemy.types import String, TypeDecorator

class HexByteString(TypeDecorator):
    """Convert Python bytestring to string with hexadecimal digits and back for storage."""

    impl = String

    def process_bind_param(self, value, dialect):
        if not isinstance(value, bytes):
            raise TypeError("HexByteString columns support only bytes values.")
        return value.hex()

    def process_result_value(self, value, dialect):
        return bytes.fromhex(value) if value else None
    
class Product_lines(db.Model):
    __tablename__ = 'product_lines'
    product_line = db.Column(db.String(50), primary_key=True,nullable=False)
    text_description = db.Column(db.String(4000), nullable=True)
    html_description = db.Column(db.String(255), nullable=True, default=None)
    image = db.Column(HexByteString, nullable=True, default=None)