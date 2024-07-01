# Projeto em desenvolvimento, inspirado em um curso.
# Aprimorando conhecimentos em APIs usando o POSTMAN.

#Importação
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "testprog"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = "login"
CORS(app)

# Modelagem
# User (id,username,password)
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable=False, unique = True)
    password = db.Column(db.String(80), nullable=False)

# Produto(id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Adicionado endpoint de autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/login", methods = ["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username = data.get("username")).first()

    if user and data.get("password") == user.password:
            login_user(user)
            return jsonify({"message": "Logged in successfully"})
    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401

@app.route("/logout", methods = ["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successfully"})


# Adicionado endpoint para adicionar o produto
@app.route("/api/products/add", methods = ["POST"])
@login_required
def add_product():
    data = request.json
    if "name" in data and "price" in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully."})
    return jsonify({"message": "Invalid product data."}), 400

# Adicionado endpoint para deletar o produto por ID
@app.route("/api/products/delete/<int:product_id>", methods = ["DELETE"])
@login_required
def delete_product(product_id):
    product=Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."})
    return jsonify({"message": "Product not found."}), 404

# Adicionado endpoint para obter detalhes do produto por ID
@app.route("/api/products/<int:product_id>", methods = ["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }), 200
    return jsonify({"message": "Product not found."}), 404

# Adicionado endpoint para atualizar o produto por ID
@app.route("/api/products/update/<int:product_id>", methods = ["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found."}), 404    

    data = request.json
    if "name" in data: 
        product.name = data["name"]

    if "price" in data:
        product.price = data["price"]
    
    if "description" in data:
        product.description = data["description"]
    db.session.commit()
    return jsonify({"message": "Product update successfully"})

# Adicionado endpoint para buscar todos os produtos do banco de dados
@app.route("/api/products", methods = ["GET"])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
        }
        product_list.append(product_data)
    return jsonify(product_list)

# Definir uma rota raiz (Página inicial) e a função que será executada quando um usuário requisitar.
@app.route("/teste")
def hello_Word():
    return "Hello Word!"

if __name__ == "__main__":
    app.run(debug=True)