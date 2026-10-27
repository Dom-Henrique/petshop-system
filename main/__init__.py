from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, login_user, current_user, login_required, login_remembered
from sqlalchemy.exc import IntegrityError
from db import db
from models import *
from functools import wraps
import os, uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///usersdata.db"
db.init_app(app) # Sempre iniciar o app
app.secret_key = 'managerpts'
log_man = LoginManager(app)
log_man.login_view = 'login' # protege o acesso de informacoes de terceiros

UPLOAD_FOLDER = os.path.join(app.root_path, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED = {"png", "jpg", "jpeg", "webp"}

@log_man.user_loader # Vai acessar um método especial da flask_login
def user_loader(id): # Busca usuário pelo id
    user = db.session.query(User).filter_by(id=id).first()
    return user

@app.route('/home')
@login_required
def home():
    userName = current_user.firstName
    products = Products.query.all()
    professionals = Professional.query.all()
    return render_template('home.html', products=products, userName=userName, professionals=professionals)

def admin_required(func):
    @wraps(func)
    @login_required
    def decorated_view(*arg, **kwargs):
        if (current_user.type_user != 1):
            abort(403)
            
        return func(*arg, **kwargs)

    return decorated_view

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
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = db.session.query(User).filter_by(email=email, password=password).first()
        if not user:
            return render_template('notlogged.html')
        
        login_user(user, remember=True) # opcao para lembrar do login por 1 ano
        return redirect(url_for('home'))

@app.route('/register_products', methods=['GET', 'POST'])
@login_required
@admin_required
def reg_products():
    if request.method=='GET':
        return render_template('adm_pages/reg-prod.html')
    elif request.method=='POST':
        file = request.files.get("product_img")
        filename = None

        if file and file.filename:
            ext = file.filename.rsplit(".", 1)[-1].lower()
            if not file or not file.filename:
                return "Image is required", 400
            if ext not in ALLOWED:
                return "Invalid file type", 400
            # unique name avoids collisions and unsafe names
            filename = f"{uuid.uuid4().hex}.{ext}"
            file.save(os.path.join(UPLOAD_FOLDER, secure_filename(filename)))       
        
        # print("CONTENT-TYPE:", request.content_type)
        # print("FILES:", request.files)
        # print("FORM:", request.form)
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_img = filename
        prod_category = request.form['category']
        product_price = request.form['product-price']
        quantity = request.form['quantity']
        
        new_product = Products(product_name=product_name, product_desc=product_desc, product_img=product_img, prod_category=prod_category, product_price=product_price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('home'))
    
    return render_template('adm_pages/reg-prod.html')

@app.route('/register_services', methods=['GET', 'POST'])
@login_required
@admin_required
def reg_services():
    if request.method=='GET':
        # Buscar os elementos
        professionals = Professional.query.all()
        profs_names = Professional.query.with_entities(Professional.prof_name).all()
        # Sempre que eu quiser rodar uma variável no Flask, preciso passar como instância uma variável
        return render_template('adm_pages/reg-serv.html', profs_names=profs_names, professionals=professionals)
    elif request.method=='POST':
        file = request.files.get("service_img")
        filename = None
        
        if (file and file.name):
            ext = file.filename.split(".", 1)[-1].lower()
            if (ext not in ALLOWED): return "invalid type", 400
            
            filename = f"{uuid.uuid4().hex}.{ext}"
            file.save(os.path.join(UPLOAD_FOLDER, secure_filename(filename)))  
        
        service_name = request.form['service_name']
        service_desc = request.form['service_desc']
        service_img = filename
        serv_category = request.form['category']
        professional = request.form['professional']
        service_price = request.form['service_price']
        
        new_service = Services(service_name=service_name, service_desc=service_desc, service_img=service_img, serv_category=serv_category, professional=professional, service_price=service_price)
        db.session.add(new_service)
        db.session.commit()
        # Depois daqui, o código morre
        return redirect(url_for('home'))

@app.route('/products')
def products():
    products = Products.query.all()
    return render_template('products.html', products=products)

@app.route('/services')
def services():
    services = Services.query.all()
    return render_template('services.html', services=services)
@admin_required
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

        return redirect(url_for('home'))
    
    return render_template('adm_pages/professionals.html')
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5152)