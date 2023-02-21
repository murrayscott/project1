DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  contact VARCHAR(255),
  telephone VARCHAR(255),
  email VARCHAR(255),
  website VARCHAR(255),
  deleted BOOLEAN
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  part_number VARCHAR(255),
  category VARCHAR(255),
  stock_qty INT,
  reorder_level INT,
  unit_multiple INT, 
  cost FLOAT,
  selling_price FLOAT,
  deleted BOOLEAN
);

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id) ON DELETE CASCADE,
  manufacturer_id INT NOT NULL REFERENCES manufacturers(id) ON DELETE CASCADE,
  deleted BOOLEAN
);