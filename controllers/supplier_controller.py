from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all() # NEW
    return render_template("suppliers/index.html", suppliers = suppliers)