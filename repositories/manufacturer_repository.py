from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturer(name, address, contact, telephone, email, web, deleted) VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.address, manufacturer.contact, manufacturer.telephone, manufacturer.email, manufacturer.web, manufacturer.deleted]
    results = run_sql( sql, values )
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['contact'],row['telephone'],row['email'],row['web'],row['deleted'])
        manufacturers.append(manufacturer)
    return manufacturers

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)