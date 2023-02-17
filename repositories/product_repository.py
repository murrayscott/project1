from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer

def save(product):
    sql = "INSERT INTO product(name, description, part_number, category, stock_qty, reorder_level, unit_multiple, cost, selling_price, deleted) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.part_number, product.category, product.stock_qty, product.reorder_level, product.unit_multiple, product.cost, product.selling_price, product.deleted]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product