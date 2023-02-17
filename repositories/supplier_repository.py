from db.run_sql import run_sql

from models.supplier import Supplier
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

def save(supplier):
    sql = "INSERT INTO suplier ( product_id, manufacturer ) VALUES ( %s, %s ) RETURNING id"
    values = [supplier.product.id, supplier.manufacturer.id]
    results = run_sql( sql, values )
    supplier.id = results[0]['id']
    return supplier