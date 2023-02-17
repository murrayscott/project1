import pdb
from models.manufacturer import Manufacturer
from models.product import Product
from models.supplier import Supplier

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

supplier_repository.delete_all()
manufacturer_repository.delete_all()
product_repository.delete_all()

product1 = Product('Cheese', XXXXX)
product_repository.save(product1)

product2 = User('Milk', XXXXX)
product_repository.save(product2)

product3 = User('Bread', XXXXX)
product_repository.save(product3)

manufacturer1 = Manufacturer('Robert Wiseman', XXXXX)
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer('Mothers Pride', XXXXX)
manufacturer_repository.save(manufacturer2)

supplier1 = Supplier(manufacturer1, product1)
supplier_repository.save(supplier1)

supplier2 = Supplier(manufacturer2, product3)
supplier_repository.save(supplier2)

supplier3 = Supplier(manufacturer1, product2)
supplier_repository.save(supplier3)

#loc = supplier_repository.location(supplier3)

pdb.set_trace()