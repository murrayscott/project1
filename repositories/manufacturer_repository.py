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
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['contact'],row['telephone'],row['email'],row['website'],row['deleted'])
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

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)