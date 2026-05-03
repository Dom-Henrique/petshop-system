# Aqui só importa a classe
from random import randint
from db import db
from flask_login import UserMixin # Serve para identificar a classe como uma classe pelo login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True) # Preencher automaticamente
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True, server_default=db.text(f"USER{randint(100000, 999999)}"))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    type_user = db.Column(db.Integer, nullable=False, server_default='2')
    
class Products(db.Model):
    __tablename__ = "products"
    prod_id = db.Column(db.Integer, primary_key=True, unique=True)
    product_name = db.Column(db.String, nullable=False, unique=True)
    product_desc = db.Column(db.String, nullable=False)
    product_img = db.Column(db.String(1000), nullable=False)
    prod_category = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
class Services(db.Model):
    __tablename__ = "services"
    serv_id = db.Column(db.Integer, primary_key=True, unique=True)
    service_name = db.Column(db.String, nullable=False)
    service_desc = db.Column(db.String, nullable=False)
    service_img = db.Column(db.String(1000), nullable=False)
    serv_category = db.Column(db.String, nullable=False)
    professional = db.Column(db.String, db.ForeignKey('professionals.prof_id'), nullable=False)
    service_price = db.Column(db.Integer, nullable=False)
    
class Professional(db.Model):
    __tablename__ = "professionals"
    prof_id = db.Column(db.Integer, primary_key=True, unique=True)
    prof_name = db.Column(db.String, nullable=False, unique=True)
    prof_ocupation = db.Column(db.String, nullable=False)