from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers( name, address, contact, telephone, email, website, deleted ) VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.address, manufacturer.contact, manufacturer.telephone, manufacturer.email, manufacturer.website, manufacturer.deleted]
    results = run_sql( sql, values )
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers WHERE deleted = FALSE"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['contact'],row['telephone'],row['email'],row['website'],row['deleted'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql( sql, values )[0]
    # check if the list returned by `run_sql( sql, values )` is empty. 
    if result is not None:
        manufacturer = Manufacturer(result['name'], result['address'],  result['contact'],  result['telephone'],  result['email'], result['website'], result['deleted'],   result['id'] )
    return manufacturer

def products(manufacturer):
    products = []
    sql = "SELECT products.* FROM products INNER JOIN suppliers ON suppliers.product_id = product.id WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)
    for row in results:
        product = Product(row['name'], row['description'], row['part_number'],row['category'],row['stock_qty'],row['reorder_level'],row['unit_multiple'],row['cost'], row['selling_price'], row['deleted'], row['id'])
        products.append(product)
    return products

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, address, contact, telephone, email, website) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.address, manufacturer.contact, manufacturer.telephone, manufacturer.email, manufacturer.website, manufacturer.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql( sql, values )