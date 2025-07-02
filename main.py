from datetime import datetime
from inventory import *
from transactions import *
from reports import *

product_stock = {}
current_balance = 1000
purchased_items = []
sold_items = []
restocked_items = []
total_payment = 0
total_sales = 0

def display_header():
    """Display system header"""
    print("\n\n")
    print("\t\t\tWeCare Wholesale System")
    print("\n")
    print("\t\tKathmandu, Nepal | Phone: 9841002456")
    print("\n")
    print("=" * 80)
    print("\n")
    print("\tWelcome to the system! We hope you have a great experience!")
    print("\n")
    print("=" * 80)
    print("\n")

def run_system():
    """Main function to run the wholesale system"""
    display_header()
    WholesaleRead(product_stock)
    
    user_name = input("Please enter customer's name: ").strip().replace(" ", "_")
    
    while True:
        phone_number = input("Please enter customer's phone number: ").strip()
        if phone_number.isdigit():
            break
        print("Invalid input! Phone number must contain only numbers. Please try again.")
    
    print("\nWelcome, " + user_name + "!")
    
    system_active = True
    while system_active:
        print("\nSystem Options:")
        print("-" * 40)
        print("\n")
        print("Press 1 to buy products")
        print("Press 2 to restock products")
        print("Press 3 to sell products")
        print("Press 4 to exit and save transaction")
        print("\n")
        print("-" * 40)
        print("\n")
        
        try:
            user_selection = int(input("Enter your choice (1-4): "))
            print("\n")
            
            if user_selection == 1:
                handle_purchase(product_stock, purchased_items, current_balance, total_payment)
            elif user_selection == 2:
                handle_restock(product_stock, restocked_items)
            elif user_selection == 3:
                handle_sell(product_stock, sold_items, current_balance, total_sales)
            elif user_selection == 4:
                WholesaleWrite(user_name, phone_number, purchased_items, sold_items, 
                              restocked_items, total_payment, total_sales, current_balance,
                              product_stock)
                system_active = False
                print("\nThank you for using our system! Have a great day!")
            else:
                print("Please select an option between 1-4!")
        except ValueError:
            print("Wrong input! Please enter a number.")

run_system()
