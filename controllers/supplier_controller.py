from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    products = product_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template("suppliers/index.html", suppliers = suppliers, products = products, manufacturers = manufacturers)

@suppliers_blueprint.route("/inventory")
def inventory():
    suppliers = supplier_repository.select_all()
    return render_template("inventory/index.html", suppliers = suppliers)

# CREATE
# POST '/suppliers'
@suppliers_blueprint.route("/suppliers",  methods=['POST'])
def create_supplier():
    product_id = request.form['product_id']
    manufacturer_id = request.form['manufacturer_id']
    product = product_repository.select(product_id)
    manufacturer =  manufacturer_repository.select(manufacturer_id)
    supplier = Supplier(product, manufacturer, False)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

# DELETE
# DELETE '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect('/suppliers') 