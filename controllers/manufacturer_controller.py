from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufactureres", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    product = manufacturer_repository.products(manufacturer)
    return render_template("manufacturers/show.html", manufacturer = manufacturer, product = product)

# CREATE NEW MANUFACTURER - POST '/manufacturers'
@manufacturers_blueprint.route("/manufacturers/add", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    address = request.form['address']
    contact = request.form['contact']
    telephone = request.form['telephone']
    email = request.form['email']
    website = request.form['website']
    manufacturer = Manufacturer(name,address,contact,telephone,email,website,False)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")

# DELETE EXISTING MANUFACTURER - DELETE '/suppliers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')