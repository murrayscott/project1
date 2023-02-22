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
    sql = "SELECT * FROM suppliers WHERE deleted = %s"
    values = [False]
    results = run_sql( sql,values )
    for row in results:
        product = product_repository.select(row['product_id'])
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        supplier = Supplier(product, manufacturer, row['deleted'], row['id'])
        suppliers.append(supplier)
    return suppliers

def delete_all():
    # ACTUALLY DELETES ALL THE RECORDS - DOES NOT UPDATE THE DELETED FLAG TO TRUE
    sql = "DELETE FROM suppliers"
    run_sql( sql )

def delete(id):
    # DOES NOT DELETE THE RECORDS - ONLY SETS THE DELETED FLAG TO TRUE AND LEAVES THE RECORD
    sql = "UPDATE suppliers SET deleted = TRUE WHERE id = %s"
    values = [id]
    run_sql( sql, values )