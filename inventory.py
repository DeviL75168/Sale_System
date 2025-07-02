# Constants for product fields
NAME = 0
BRAND = 1
QUANTITY = 2
PRICE = 3
ORIGIN = 4

def WholesaleRead(product_stock):
    """Read product data from inventory file"""
    try:
        stock_file = open("inventories.txt", "r")
        item_number = 1
        for item_line in stock_file:
            item_details = item_line.strip().split(",")
            product_stock[item_number] = item_details
            item_number += 1
        stock_file.close()
    except FileNotFoundError:
        print("Notice: inventories.txt not found. Starting with empty inventory.")

def save_inventory_to_file(product_stock):
    """Save current inventory to file"""
    with open("inventories.txt", "w") as inventory_file:
        for product in product_stock.values():
            inventory_file.write(",".join(product) + "\n")

def display_products(product_stock):
    """Show all products in table format"""
    print("\n" + "*" * 80)
    print("ID\tName\t\tBrand\t\tQty\tPrice\tOrigin")
    print("*" * 80)
    for item_id, item_info in product_stock.items():
        line = str(item_id).ljust(3) + "\t"
        line += str(item_info[NAME]).ljust(12) + "\t"
        line += str(item_info[BRAND]).ljust(8) + "\t"
        line += str(item_info[QUANTITY]).rjust(3) + "\t"
        line += str(item_info[PRICE]).rjust(5) + "\t"
        line += str(item_info[ORIGIN]).ljust(10)
        print(line)
    print("*" * 80)

def get_product_details(product_stock, product_id):
    """Get product details using product ID"""
    if product_id in product_stock:
        product = product_stock[product_id]
        return {
            'name': product[NAME],
            'brand': product[BRAND],
            'quantity': int(product[QUANTITY]),
            'price': int(product[PRICE]),
            'origin': product[ORIGIN]
        }
    return None