# import module
from tabulate import tabulate


# ========The beginning of the class==========
# It creates a class called Shoe.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """The function __init__() is a special function in Python classes. It is run as soon as an object of a class is
        instantiated. The method is useful to do any initialization you want to do with your object.
        :param country: The country where the order was placed
        :param code: The code of the product
        :param product: The name of the product
        :param cost: The cost of the product in the country
        :param quantity: the number of items sold"""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """The function get_cost() returns the cost of the item
        :return: The cost of the item."""
        return self.cost

    def get_quantity(self):
        """It returns the quantity of the item.
        :return: The quantity of the item."""
        return self.quantity

    def update(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """This function reads the data from the inventory.txt file and appends it to the shoe_list"""
    try:
        file_name = open('inventory.txt', 'r')
        file_name.readline()

        for line in file_name:
            shoes = line.strip().split(',')
            shoe_list.append(Shoe(shoes[0], shoes[1], shoes[2], float(shoes[3]), int(shoes[4])))

    except FileNotFoundError:
        print("The file does not exist")


def update_file():
    """This function opens the inventory.txt file and writes the data from the shoe_list to the file"""
    file = open('inventory.txt', 'w')
    data = "Country,Code,Product,Cost,Quantity\n"
    file.write(data)
    for shoe in shoe_list:
        file.write(shoe.update() + '\n')


def capture_shoes():
    """This function allows the user to input the country, code, product, cost, and quantity of a shoe and then adds
    it to the shoe_list."""
    country = input("What country is the shoe from?: ")
    code = input("What is the code for the shoe?: ")
    product = input("What is the name of the shoe?: ")
    cost = input("How much does the shoe cost?: ")
    quantity = input("What quantity are you buying of the shoe?: ")

    shoe_list.append(Shoe(country, code, product, cost, quantity))
    update_file()
    print("New shoe has been added.")


def view_all():
    """It loops through the shoe_list and appends the country, code, product, cost, and quantity of each shoe to a
    list called data. Then it prints the data in a table using the tabulate function """
    data = []

    for shoe in shoe_list:
        data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(data, headers=head, tablefmt='fancy_grid'))


def re_stock():
    """This function will find the shoe with the least amount of quantity and ask the user if they would like to
    restock that shoe """
    shoe_pos = 0
    qty = shoe_list[shoe_pos].quantity

    for pos, shoe in enumerate(shoe_list):
        if qty > shoe.quantity:
            shoe_pos = pos
            qty = shoe.quantity

    print(f"{shoe_list[shoe_pos].product} has {qty} pairs of shoes left")
    print(f"{shoe_list[shoe_pos].product} needs to be re-stocked.")
    restock = input("Would you like to restock this shoe?(yes or no):").lower()

    if restock == 'yes':
        quantity = input("How many pairs of shoes would you like to buy?:")
        result = qty + int(quantity)
        print(result)
        shoe_list[shoe_pos].quantity = result
        print(result)
        print(f"{shoe_list[shoe_pos].product} has been restocked")
        for shoe in shoe_list:
            print(shoe)
    elif restock == 'no':
        print("Goodbye")
    else:
        print("Invalid entry")

    update_file()


def search_shoe():
    """It asks the user to input a shoe code, then it searches the shoe list for a shoe with that code, and if it
    finds one, it prints it """
    search = input("Enter the shoe code for the shoe you are looking for: ")
    shoe_pos = 0

    for count, shoe in enumerate(shoe_list):
        if search == shoe.code:
            shoe_pos = count

    print(shoe_list[shoe_pos])


def value_per_item():
    """It loops through the shoe_list, and for each shoe, it calculates the value of the stock, and prints it out"""
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"The total stock of the {shoe.product}, has a value of R{value}")


def highest_qty():
    """It loops through the list of shoes and finds the shoe with the highest quantity"""
    shoe_pos = 0
    qty = shoe_list[shoe_pos].quantity

    for pos, shoe in enumerate(shoe_list):
        if qty < shoe.quantity:
            shoe_pos = pos
            qty = shoe.quantity

    print(f"{shoe_pos}. {shoe_list[shoe_pos]}")


# ==========Main Menu=============
menu = input("Select one of the following options:\ncs - capture shoe\nva - view all\nr - "
             "re-stock\nss - search shoe\nv - value per item\nh - highest quantity\nSelection: ")

# Reading the data from the inventory.txt file and appending it to the shoe_list.
read_shoes_data()

# A while loop that will keep running until the user enters a valid input.
while True:
    if menu == 'cs':
        capture_shoes()
        break
    elif menu == 'va':
        view_all()
        break
    elif menu == 'r':
        re_stock()
        break
    elif menu == 'ss':
        search_shoe()
        break
    elif menu == 'v':
        value_per_item()
        break
    elif menu == 'h':
        highest_qty()
        break
    else:
        print("Invalid entry")
        break
