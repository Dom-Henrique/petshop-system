from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
from sqlalchemy.exc import IntegrityError
from db import db
from models import *
from functions import recog_voice

app = Flask(__name__) # Serve para localizar o nome do arquivo
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///usersdata.db"
db.init_app(app) # Sempre iniciar o app
app.secret_key = 'manager'
log_man = LoginManager(app)
log_man.login_view = 'login'

@log_man.user_loader # Vai acessar um método especial da flask_login
def user_loader(id): # Busca usuário pelo id
    user = db.session.query(User).filter_by(id=id).first()
    return user

@app.route('/home')
def home():
    products = Products.query.all()
    return render_template('home.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="GET":
        return render_template('signup.html')
    elif request.method=="POST":
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        type_user = request.form['type_user']
        
        new_user = User(firstName=firstName, lastName=lastName, username=username, email=email, password=password, type_user=type_user)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            return render_template('error.html')
        
        login_user(new_user)
        
        return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST']) # methods servem para informar ao navegador quais tipos de atividades devem ser feitas com os dados enviados.
def login():
    if request.method == "GET":
        return render_template('login.html', recog_voice=recog_voice)
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = db.session.query(User).filter_by(email=email, password=password).first()
        if not user:
            return render_template('notlogged.html')
        
        login_user(user)
        return redirect(url_for('home'))

@app.route('/register_products', methods=['GET', 'POST'])
def reg_products():
    if request.method=='GET':
        return render_template('adm_pages/reg-prod.html')
    elif request.method=='POST':
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        prod_category = request.form['category']
        product_price = request.form['product-price']
        quantity = request.form['quantity']
        
        new_product = Products(product_name=product_name, product_desc=product_desc, prod_category=prod_category, product_price=product_price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('reg_products'))
    
    return render_template('adm_pages/reg-prod.html')
        
@app.route('/register_services', methods=['GET', 'POST'])
def reg_services():
    if request.method=='GET':
        # Buscar os elementos
        professionals = Professional.query.all()
        profs_names = Professional.query.with_entities(Professional.prof_name).all()
        # Sempre que eu quiser rodar uma variável no Flask, preciso passar como instância uma variável
        return render_template('adm_pages/reg-serv.html', profs_names=profs_names, professionals=professionals)
    elif request.method=='POST':
        service_name = request.form['service_name']
        service_desc = request.form['service_desc']
        serv_category = request.form['category']
        professional = request.form['professional']
        service_price = request.form['service_price']
        
        new_service = Services(service_name=service_name, service_desc=service_desc, serv_category=serv_category, professional=professional, service_price=service_price)
        db.session.add(new_service)
        db.session.commit()
        # Depois daqui, o código morre
        return redirect(url_for('reg_services'))

@app.route('/products')
def products():
    products = Products.query.all()
    return render_template('products.html', products=products)

@app.route('/services')
def services():
    services = Services.query.all()
    return render_template('services.html', services=services)

@app.route('/professionals', methods=['GET', 'POST'])
def professionals():
    if request.method=='GET':
        return render_template('adm_pages/professionals.html')
    elif request.method=='POST':
        prof_name = request.form['prof_name']
        prof_ocupation = request.form['prof_ocupation']

        newProf = Professional(prof_name=prof_name, prof_ocupation=prof_ocupation)
        db.session.add(newProf)
        db.session.commit()

        return redirect(url_for('professionals'))
    
    return render_template('adm_pages/professionals.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5152)