from flask import jsonify, request, abort
from service.models import Product, Category
from service import app

@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id '{product_id}' was not found.")
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_products(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id '{product_id}' was not found.")
    product.deserialize(request.get_json())
    product.update()
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    product = Product.find(product_id)
    if product:
        product.delete()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    products = []
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        category_value = getattr(Category, category.upper(), None)
        if category_value:
            products = Product.find_by_category(category_value)
    elif available:
        available_value = available.lower() in ["true", "1", "t"]
        products = Product.find_by_availability(available_value)
    else:
        products = Product.all()

    results = [p.serialize() for p in products]
    return jsonify(results), 200
