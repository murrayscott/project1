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

product1 = Product('Nutella','Hazelnut chocolate spread', '80177173', 'Condiments', 23, 10, 12, 2.99, 1.78, False)
product_repository.save(product1)

product2 = Product('6P Milk','Semi Skimmed Milk','4088600538044','Dairy', 62, 50, 48, 3.03, 3.40, False )
product_repository.save(product2)

product3 = Product('4P Milk','Semi Skimmed Milk','4088600538032','Dairy', 62, 50, 48, 2.03, 2.40, False )
product_repository.save(product3)

product4 = Product('2P Milk','Semi Skimmed Milk','4088600538872','Dairy', 62, 50, 48, 1.10, 1.40, False )
product_repository.save(product4)

product5 = Product('Mothers Pride Superseeded Sliced', 'Mixed Grain Sliced Loaf','5054781498063', 'Grain', 45, 40, 12, 1.45, 1.89, False)
product_repository.save(product5)

manufacturer1 = Manufacturer('Robert Wiseman', 'Moorfield Industrial Estate, Kilmarnock. KA2 0BA', 'Richard Fields', '01563 521376', 'orders@muller.co.uk','www.muller.co.uk', False)
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer('Allied Bakeries','180 Glentanar Rd, Glasgow. G22 7XS', 'Barry Brownbread', '0141 347 4222', 'sales@alliedbakeries.co.uk', 'www.alliedbakeries.co.uk', False)
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer('Ferrero', '889 Greenford Rd, Greenford. UB6 0HE','Tracy Nutford', '020 8868 4000','orders@ferrero.co.uk', 'www.fererro.co.uk', False )
manufacturer_repository.save(manufacturer3)

supplier1 = Supplier( product2, manufacturer1, False)
supplier_repository.save(supplier1)

supplier2 = Supplier( product3, manufacturer1, False)
supplier_repository.save(supplier2)

supplier3 = Supplier( product4, manufacturer1, False)
supplier_repository.save(supplier3)

supplier4 = Supplier( product5, manufacturer2, False)
supplier_repository.save(supplier4)

supplier5 = Supplier( product1, manufacturer3, False)
supplier_repository.save(supplier5)

pdb.set_trace()