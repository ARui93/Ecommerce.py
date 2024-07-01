# Projeto em desenvolvimento, inspirado em um curso.
# Aprimorando conhecimentos em APIs usando o POSTMAN.

#Importação
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)

# Modelagem
# Produto(id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Adicionado endpoint para adicionaro produto
@app.route("/api/products/add", methods = ["POST"])
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


# Definir uma rota raiz (Página inicial) e a função que será executada quando um usuário requisitar.
@app.route("/teste")
def hello_Word():
    return "Hello Word!"

if __name__ == "__main__":
    app.run(debug=True)