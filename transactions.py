from inventory import get_product_details, display_products, save_inventory_to_file

def handle_purchase(product_stock, purchased_items, current_balance, total_payment):
    """Handle product purchase process"""
    continue_purchasing = True
    
    while continue_purchasing:
        print("\nYour available balance: Rs." + str(current_balance))
        display_products(product_stock)
        
        try:
            chosen_id = int(input("\nEnter the ID of product you want to buy: "))
            product = get_product_details(product_stock, chosen_id)
            
            if not product:
                print("Please enter a valid product ID!")
                continue
                
            chosen_quantity = int(input("Enter how many you want to purchase: "))
            if chosen_quantity <= 0:
                print("Quantity must be a positive number!")
                continue
                
            print("\nProduct Details:")
            print("Name: " + product['name'])
            print("Brand: " + product['brand'])
            print("Origin: " + product['origin'])
            print("Price: Rs." + str(product['price']))
            print("Available: " + str(product['quantity']))
            
            if chosen_quantity <= product['quantity']:
                cost = chosen_quantity * product['price']
                
                if cost <= current_balance:
                    free_items = chosen_quantity // 3
                    total_to_deduct = chosen_quantity - free_items
                    
                    old_quantity = product['quantity']
                    new_quantity = old_quantity - total_to_deduct
                    product_stock[chosen_id][2] = str(new_quantity)
                    current_balance -= cost
                    total_payment += cost
                    
                    purchased_items.append([
                        product['name'], 
                        chosen_quantity, 
                        product['price'], 
                        cost, 
                        product['brand'], 
                        product['origin'],
                        old_quantity,
                        new_quantity
                    ])
                    save_inventory_to_file(product_stock)
                    
                    print("\nPurchased " + str(chosen_quantity) + " " + product['name'] + "(s) for Rs." + str(cost))
                    print("Quantity updated from " + str(old_quantity) + " to " + str(new_quantity))
                    if free_items > 0:
                        print("Special offer! You get " + str(free_items) + " " + product['name'] + "(s) for free!")
                    print("Remaining balance: Rs." + str(current_balance))
                    
                    more_items = input("\nWould you like to buy more items? (yes/no): ").lower()
                    if more_items != "yes":
                        continue_purchasing = False
                else:
                    print("Insufficient funds for this purchase!")
                    continue_purchasing = False
            else:
                print("Not enough stock available for this item!")
        except ValueError:
            print("Please enter numbers only!")
    return current_balance, total_payment

def handle_restock(product_stock, restocked_items):
    """Handle product restocking process"""
    display_products(product_stock)
    
    try:
        restock_id = int(input("\nEnter product ID to restock: "))
        product = get_product_details(product_stock, restock_id)
        
        if not product:
            print("Wrong product ID entered!")
            return
            
        restock_quantity = int(input("Enter quantity to add: "))
        if restock_quantity <= 0:
            print("Quantity must be a positive number!")
            return
        
        old_quantity = product['quantity']
        new_quantity = old_quantity + restock_quantity
        product_stock[restock_id][2] = str(new_quantity)
        
        restock_value = restock_quantity * product['price']
        restocked_items.append([
            product['name'],
            restock_quantity,
            product['price'],
            restock_value,
            product['brand'],
            product['origin'],
            old_quantity,
            new_quantity
        ])
        
        save_inventory_to_file(product_stock)
        
        print("\nSuccessfully restocked " + product['name'])
        print("Added " + str(restock_quantity) + " items worth Rs." + str(restock_value))
        print("Quantity updated from " + str(old_quantity) + " to " + str(new_quantity))
        print("Inventory file updated immediately.")
    except ValueError:
        print("Please enter numeric values only!")

def handle_sell(product_stock, sold_items, current_balance, total_sales):
    """Handle product selling process"""
    display_products(product_stock)
    
    try:
        sell_id = int(input("\nEnter product ID to sell: "))
        product = get_product_details(product_stock, sell_id)
        
        if not product:
            print("Wrong product ID entered!")
            return
            
        sell_quantity = int(input("Enter quantity to sell: "))
        if sell_quantity <= 0:
            print("Quantity must be a positive number!")
            return
        
        if sell_quantity <= product['quantity']:
            old_quantity = product['quantity']
            new_quantity = old_quantity - sell_quantity
            product_stock[sell_id][2] = str(new_quantity)
            sale_value = sell_quantity * product['price']
            current_balance += sale_value
            total_sales += sale_value
            
            sold_items.append([
                product['name'], 
                sell_quantity, 
                product['price'], 
                sale_value, 
                product['brand'], 
                product['origin'],
                old_quantity,
                new_quantity
            ])
            save_inventory_to_file(product_stock)
            
            print("\nSuccessfully sold " + str(sell_quantity) + " " + product['name'] + "(s)")
            print("Quantity changed from " + str(old_quantity) + " to " + str(new_quantity))
            print("Added Rs." + str(sale_value) + " to your balance")
            print("New balance: Rs." + str(current_balance))
        else:
            print("Cannot sell " + str(sell_quantity) + " items. Only " + str(product['quantity']) + " available.")
    except ValueError:
        print("Please enter numeric values only!")
    return current_balance, total_sales