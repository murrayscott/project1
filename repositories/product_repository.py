from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer

def save(product):
    sql = "INSERT INTO products( name, description, part_number, category, stock_qty, reorder_level, unit_multiple, cost, selling_price, deleted ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.description, product.part_number, product.category, product.stock_qty, product.reorder_level, product.unit_multiple, product.cost, product.selling_price, product.deleted]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['description'], row['part_number'],row['category'],row['stock_qty'],row['reorder_level'],row['unit_multiple'],row['cost'], row['selling_price'], row['deleted'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql( sql, values )
    # check if the list returned by `run_sql( sql, values )` is empty. 
    if results:
        result = results[0]
        product = Product(result['name'], result['description'], result['part_number'], result['category'], result['stock_qty'], result['reorder_level'], result['unit_multiple'], result['cost'], result['selling_price'], result['deleted'], result['id'] )
    return product

def manufacturers(product):
    manufacturers = []

    sql = "SELECT manufacturers.* FROM manufacturers INNER JOIN suppliers ON suppliers.manufacturer_id = manufacturer.id WHERE product_id = %s"
    values = [product.id]
    results = run_sql( sql, values )
    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['contact'],row['telephone'],row['email'],row['website'],row['deleted'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)