Stock Inventory Management App

Summary:

Inventory management system that allows stock tracking of products across multiple manufacturers and is configurable to suit a variets of businesses. It supports the supply of a single product from multiple manufacturing sources.

Created using the following applications: python, flask, postgresql

Installation:
Copy all files and folders from the repository into a new folder.
Ensure Postgresql is installed this can be done through the Pip installer.
Open terminal.
Create a database by typing createdb 'db/store_inventory'.
Type the  following 'psql -d store_inventory -f db/store_inventory.sql' to set up the table structure within the database.
Start Flask by entering 'flask run' at the terminal prompt.
Using your browser type '127.0.0.1:4999' in the address bar. The 4999 port number can be modified by editing the .flaskenv file in the main folder if required.

