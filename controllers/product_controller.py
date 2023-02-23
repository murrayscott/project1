from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

# CREATE NEW PRODUCT - POST '/products'
@products_blueprint.route("/products/add", methods=['POST'])
def create_product():
    name = request.form['name']
    description = request.form['description']
    part_number = request.form['part_number']
    category =  request.form['category']
    stock_qty = int(request.form['stock_qty'])
    reorder_level = int(request.form['reorder_level'])
    unit_multiple = int(request.form['unit_multiple'])
    cost = float(request.form['cost'])
    selling_price = float(request.form['selling_price'])
    product = Product(name,description,part_number,category,stock_qty,reorder_level,unit_multiple,cost,selling_price,False)
    product_repository.save(product)
    return redirect("/products")

# EDIT PRODUCT - GET '/products/<id>/edit'
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_products(id):
    product = product_repository.select(id)
    return render_template('products/edit.html', product = product)

# UPDATE PRODUCT - PUT '/products/<id>/update'
@products_blueprint.route("/products/<id>/update", methods=['POST'])
def update_products(id):
    name = request.form['name']
    description = request.form['description']
    part_number = request.form['part_number']
    category = request.form['category']
    stock_qty = request.form['stock_qty']
    reorder_level = request.form['reorder_level']
    unit_multiple = request.form['unit_multiple']
    cost = request.form['cost']
    selling_price = request.form['selling_price']
    product = Product(name,description,part_number,category,stock_qty,reorder_level,unit_multiple,cost,selling_price,False,id)
    product_repository.update(product)
    return redirect('/products')

# DELETE SINGLE PRODUCT BY ID - DELETE '/products/<id>'
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_task(id):
    product_repository.delete(id)
    return redirect('/products')