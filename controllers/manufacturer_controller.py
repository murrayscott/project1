from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufactureres", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

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

# EDIT MANUFACTURER - GET '/manufacturers/<id>/edit'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

# UPDATE MANUFACTURER - PUT '/manufacturers/<id>/update'
@manufacturers_blueprint.route("/manufacturers/<id>/update", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    address = request.form['address']
    contact = request.form['contact']
    telephone = request.form['telephone']
    email = request.form['email']
    website = request.form['website']
    manufacturer = Manufacturer(name,address,contact,telephone,email,website,False,id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

# DELETE EXISTING MANUFACTURER - DELETE '/suppliers/<id>/delete'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')