from db.run_sql import run_sql

from models.supplier import Supplier
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

def save(supplier):
    sql = "INSERT INTO suppliers ( product_id, manufacturer_id, deleted ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [supplier.product.id, supplier.manufacturer.id, supplier.deleted]
    results = run_sql( sql, values )
    supplier.id = results[0]['id']
    return supplier

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        product = product_repository.select(row['product_id'])
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        supplier = Supplier(product, manufacturer, row['id'])
        suppliers.append(supplier)
    return suppliers

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)