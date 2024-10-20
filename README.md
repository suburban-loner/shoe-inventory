# Shoe-Inventory

This is a Python program designed to help manage a shoe inventory by reading data from a text file (inventory.txt). The program allows users to perform tasks such as adding new shoes, restocking existing shoes, searching for shoes by their code, and calculating the total value of each item in stock.

## Features
The system provides the following functionalities:

View All Shoes: Displays all shoes in the inventory with their details (country, code, product, cost, and quantity).
Capture New Shoe: Allows users to add new shoe entries to the inventory.
Restock Shoe: Identifies the shoe with the lowest stock quantity and allows the user to add more to its stock.
Search Shoe by Code: Lets the user search for a shoe by its unique code and view its details.
Display Value per Item: Calculates and displays the total value for each shoe in stock (calculated as cost * quantity).
Highest Quantity: Identifies and displays the shoe with the highest quantity in stock, indicating that it is for sale.

## Shoe Class
The program uses a Shoe class to represent each shoe. The class contains the following attributes:

country: The country where the shoe is manufactured.
code: The unique product code.
product: The name of the shoe product.
cost: The cost of the shoe.
quantity: The number of units in stock.
Methods in Shoe Class
get_cost(): Returns the cost of the shoe.
get_quantity(): Returns the quantity in stock for the shoe.
__str__(): Returns a string representation of the shoe's details (country, code, product, cost, and quantity).

## Data Storage
The shoe inventory data is stored in a text file called inventory.txt.
