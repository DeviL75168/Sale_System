from datetime import datetime
from inventory import save_inventory_to_file

def WholesaleWrite(customer_name, phone_number, purchased_items, sold_items, 
                  restocked_items, total_payment, total_sales, current_balance,
                  product_stock):
    """Save transaction details to files"""
    print("\n" + "=" * 80)
    print("Transaction Date/Time: " + datetime.now().ctime())
    print("Customer: " + customer_name)
    print("Phone: " + phone_number)
    
    # Purchase Details
    if purchased_items:
        print("\nPurchase Details:")
        print("-" * 80)
        print("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal")
        print("-" * 80)
        for item in purchased_items:
            item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
            brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
            
            item_line = item[0] + item_tabs
            item_line += item[4] + brand_tabs
            item_line += item[5] + "\t"
            item_line += str(item[1]) + "\t"
            item_line += str(item[6]) + "\t"
            item_line += str(item[7]) + "\t"
            item_line += "Rs." + str(item[2]) + "\t"
            item_line += "Rs." + str(item[3])
            print(item_line)
        print("-" * 80)
        print("Total Purchases: Rs." + str(total_payment))
    
    # Sales Details
    if sold_items:
        print("\nSales Details:")
        print("-" * 80)
        print("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal")
        print("-" * 80)
        for item in sold_items:
            item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
            brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
            
            item_line = item[0] + item_tabs
            item_line += item[4] + brand_tabs
            item_line += item[5] + "\t"
            item_line += str(item[1]) + "\t"
            item_line += str(item[6]) + "\t"
            item_line += str(item[7]) + "\t"
            item_line += "Rs." + str(item[2]) + "\t"
            item_line += "Rs." + str(item[3])
            print(item_line)
        print("-" * 80)
        print("Total Sales: Rs." + str(total_sales))
    
    # Restock Details
    if restocked_items:
        print("\nRestock Details:")
        print("-" * 80)
        print("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal")
        print("-" * 80)
        for item in restocked_items:
            item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
            brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
            
            item_line = item[0] + item_tabs
            item_line += item[4] + brand_tabs
            item_line += item[5] + "\t"
            item_line += str(item[1]) + "\t"
            item_line += str(item[6]) + "\t"
            item_line += str(item[7]) + "\t"
            item_line += "Rs." + str(item[2]) + "\t"
            item_line += "Rs." + str(item[3])
            print(item_line)
        print("-" * 80)
    
    print("\nNet Total: Rs." + str(total_sales - total_payment))
    print("Remaining Balance: Rs." + str(current_balance))
    print("=" * 80)
 
    # Save to receipt file
    with open("receipt_" + customer_name + ".txt", "w") as receipt_file:
        receipt_file.write("Transaction Date/Time: " + datetime.now().ctime() + "\n")
        receipt_file.write("Customer: " + customer_name + "\n")
        receipt_file.write("Phone: " + phone_number + "\n")
        
        if purchased_items:
            receipt_file.write("\nPurchase Details:\n")
            receipt_file.write("-" * 80 + "\n")
            receipt_file.write("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal\n")
            receipt_file.write("-" * 80 + "\n")
            for item in purchased_items:
                item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
                brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
                
                item_line = item[0] + item_tabs
                item_line += item[4] + brand_tabs
                item_line += item[5] + "\t"
                item_line += str(item[1]) + "\t"
                item_line += str(item[6]) + "\t"
                item_line += str(item[7]) + "\t"
                item_line += "Rs." + str(item[2]) + "\t"
                item_line += "Rs." + str(item[3]) + "\n"
                receipt_file.write(item_line)
            receipt_file.write("-" * 80 + "\n")
            receipt_file.write("Total Purchases: Rs." + str(total_payment) + "\n")
        
        if sold_items:
            receipt_file.write("\nSales Details:\n")
            receipt_file.write("-" * 80 + "\n")
            receipt_file.write("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal\n")
            receipt_file.write("-" * 80 + "\n")
            for item in sold_items:
                item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
                brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
                
                item_line = item[0] + item_tabs
                item_line += item[4] + brand_tabs
                item_line += item[5] + "\t"
                item_line += str(item[1]) + "\t"
                item_line += str(item[6]) + "\t"
                item_line += str(item[7]) + "\t"
                item_line += "Rs." + str(item[2]) + "\t"
                item_line += "Rs." + str(item[3]) + "\n"
                receipt_file.write(item_line)
            receipt_file.write("-" * 80 + "\n")
            receipt_file.write("Total Sales: Rs." + str(total_sales) + "\n")
        
        if restocked_items:
            receipt_file.write("\nRestock Details:\n")
            receipt_file.write("-" * 80 + "\n")
            receipt_file.write("Item\t\tBrand\t\tOrigin\tQty\tBefore\tAfter\tPrice\tTotal\n")
            receipt_file.write("-" * 80 + "\n")
            for item in restocked_items:
                item_tabs = "\t" if len(item[0]) > 7 else "\t\t"
                brand_tabs = "\t" if len(item[4]) > 7 else "\t\t"
                
                item_line = item[0] + item_tabs
                item_line += item[4] + brand_tabs
                item_line += item[5] + "\t"
                item_line += str(item[1]) + "\t"
                item_line += str(item[6]) + "\t"
                item_line += str(item[7]) + "\t"
                item_line += "Rs." + str(item[2]) + "\t"
                item_line += "Rs." + str(item[3]) + "\n"
                receipt_file.write(item_line)
            receipt_file.write("-" * 80 + "\n")
        
        receipt_file.write("\nNet Total: Rs." + str(total_sales - total_payment) + "\n")
        receipt_file.write("Remaining Balance: Rs." + str(current_balance) + "\n")
        receipt_file.write("=" * 80 + "\n")

    save_inventory_to_file(product_stock)