from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufactureres", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() # NEW
    return render_template("manufacturer/index.html", manufacturers = manufacturers)