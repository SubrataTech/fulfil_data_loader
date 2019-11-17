from configuration_file import db


class UserTable(db.Model):
    __tablename__ = 'user_data'
    id = db.Column('id', db.Integer, primary_key=True)
    u_name = db.Column('u_name', db.String(50))
    u_sku = db.Column('u_sku', db.String(10))
    u_description = db.Column('u_description', db.String(1500))
