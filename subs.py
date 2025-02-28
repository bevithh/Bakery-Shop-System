#Greeting the user
print("""
                                                WELCOME TO SUBS
                                @@@@@@@@@@@@@        SUBS         @@@@@@@@@@@@@

""")

#indicate the text file
infile = open('Products.txt','r')
products_lst =[]

for line in infile:
    line = line.rstrip() # remove the '\n'
    bread_lst = line.split(',') # create bread as a list of info
    products_lst.append(bread_lst) # add each bread into product list


infile.close()
ans = "y"
condition = True
#define bread_list function
def bread_list():
    print("Code \t Name \t\t\t\t Price \t\t Status")
    print("---- \t ---- \t\t\t\t ----- \t\t ------")
    for r in range(len(products_lst)):
        for c in range(len(products_lst[r])):
            print(products_lst[r][c], "\t\t", end="")
        print()


def setup_list():
    ans = 'y'

    while ans == "y":
        update_code = input("Enter new code: ")
        exist = False
        for sublist in products_lst:
            if sublist[0]==update_code:
                exist = True
                break

        if exist:
            print("This code already exists. Please enter a new code.")
            continue

        update_name = input("Enter bread name: ")
        update_price = float(input("Enter price: $"))
        update_status = input("Enter status: ")
        products_lst.append([update_code, update_name, update_price, update_status])
        print("Product added successfully!")
        ans = input("Do you want to add more pastry(y/n)?: ")
        if ans != 'y':
            break

    with open("Products.txt", "w") as f:
        for product in products_lst:
            f.write(",".join(map(str, product)) + "\n")
    print(f"code:{update_code},name:{update_name},price:{update_price},status:{update_status}")
    print(products_lst)
    f.close()


def update_list():

    def search_item_code(code):
        for product in products_lst:
            if code in product:
                return product
    while True:
        code = input("Enter item code to search: ")
        if code == 'q':
            break
        item = search_item_code(code)

        if item in products_lst:
            print(f"Item: {item[1]}, Price: {item[2]}, Status: {item[3]}")
            new_price = input("Enter new price (press N to keep current price): ")
            if new_price != "N":
                item[2] = float(new_price)
            new_status = input("Enter new status (press N to keep current status): ")
            if new_status != "N":
                item[3] = str(new_status)

            with open("Products.txt", "w") as f:
                for product in products_lst:
                    f.write(",".join(map(str, product)) + "\n")
            print(f"Item: {item[1]}, Price: {item[2]}, Status: {item[3]}")
            print(products_lst)
            f.close()
            break

        else:
            print("Item is not found")


def reload_pastry():

    print("Code \t Name \t\t\t\t Price \t\t Status")
    print("---- \t ---- \t\t\t\t ----- \t\t ------")
    for r in range(len(products_lst)):
        for c in range(len(products_lst[r])):
            print(products_lst[r][c], "\t\t", end="")
        print()

    with open("Products.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            product = line.strip().split(",")
            products_lst.append(product)
    print(products_lst)
    print("Pastry details re-loaded successfully!")
    f.close()

from datetime import datetime

now = datetime.now()
orders_lst=[]
def create_order():

        discount_scheme = {50: 0.1, 75: 0.15,  100: 0.2}

        # Define the delivery fee
        delivery_fee = 5

        # Initialize the order
        order = []

        # Take input from user until "X" or "x" is entered
        while True:
            input_str = input("Enter item and quantity (x or X to finish): ")
            if input_str.lower() == "x":
                break
            input_lst = input_str.split(",")
            if len(input_lst) != 2:
                print("Invalid input, please enter item code and quantity separated by comma.")
                continue
            code = input_lst[0].strip().upper()
            quantity = input_lst[1].strip()
            found = False
            for product in products_lst:
                if product[0] == code and product[3] == "Available":
                    found = True
                    price = float(product[2])
                    item_total = price * int(quantity)
                    order.append([code, product[1], quantity, price, item_total])
                    break
            if not found:
                print("Invalid item code or item is not available.")

        # Calculate the order summary
        subtotal = sum(item[4] for item in order)
        discount_rate = 0
        for limit, rate in discount_scheme.items():
            if subtotal >= limit:
                discount_rate = rate
        discount = subtotal * discount_rate
        if subtotal >= 50:
            delivery = 0
        else:
            delivery = delivery_fee
        total_due = subtotal - discount + delivery

        # Display the order summary
        print("Item\t\tQuantity\tPrice\tAmount")
        for item in order:
            print(f"{item[1]}\t{item[2]}\t${item[3]:.2f}\t${item[4]:.2f}")
        print(f"Subtotal\t\t\t${subtotal:.2f}")
        if delivery == 0:
            print("Delivery\t\t\tFree")
        else:
            print(f"Delivery\t\t\t${delivery:.2f}")
        if discount_rate > 0:
            print(f"Discount\t\t\t{discount_rate * 100:.0f}%")
            print(f"Total Due\t\t\t${total_due:.2f}")


        while True:
            confirm_order = input("Proceed to order (y/n): ")
            if confirm_order.lower() == "n":
                print("Order cancelled.")
                return


            else:
                name = input("Enter name: ")
                address = input("Enter delivery address: ")

                import datetime
                import random

# Get the current date in YYYYMMDD format
                date_str = datetime.datetime.now().strftime('%Y%m%d')

# Generate a random number between 10 and 999 for the XX part of the Order ID
                random_num = str(random.randint(1, 999))

# Combine the date string and random number to form the Order ID
                order_id = f"{date_str}-{random_num}"
                payment_status = "pending"
                status = "pending"
                orders_lst.append([order_id, name, address, total_due, payment_status, status])
                print("Order created and Order ID is {}".format(order_id))
                print(orders_lst)
                break



def cancel_order():

    def search_order_order_id(order_id):
        for order in orders_lst:
            if order_id in order[0]:
                return order
    while True:
        order_id = input("Enter Order ID to cancel (or X to go back to menu): ")
        if order_id.lower() == "x":
            break

        order = search_order_order_id(order_id)
        found = False
        if order:
            if order[4] == "Payment Received":
                print("Order cannot be cancelled as it is already in", order[4], "status.")
            elif order[4] == "pending":
                print("Order", order[0], "has been cancelled.")
                order[4] = "Cancelled"
                order[5] = "Cancelled"
        else:
            print("No order found with the given Order ID.")


def update_payment():
    order_id = input("Enter Order ID to receive payment: ")
    found = False
    for order in orders_lst:
        if order[0] == order_id:
            if order[4] == "Payment Received":
                print("Payment already received for this order.")
                break
            elif order[4] == "Cancelled":
                print("Order has been cancelled. Payment cannot be received.")
                break
            else:
                paynow_reference = input("Enter Paynow Reference: ")
                order[4] = "Payment Received"
                order[5]="Baking"
                print("Payment received for order", order_id)
                print(orders_lst)
                found = True
                break

    if not found:
        print("No order found with the given Order ID.")



def update_order_status():
    order_id = input("Enter Order ID to update status: ")
    found = False
    for order in orders_lst:
        if order[0] == order_id:
            found = True
            if order[5] == "Ready to ship":
                print("Order already marked as 'Ready to ship'.")
                break
            elif order[4] != "Payment Received":
                print("Order payment has not been received yet. Cannot update status.")
                break
            else:
                order[5] = "Ready to ship"
                print("Order status updated to 'Ready to ship' for Order ID", order[0])
                print(orders_lst)
                break

    if not found:
        print("No order found with the given Order ID.")

import datetime

def tdy_lst():
    today = datetime.date.today().strftime("%Y%m%d")
    orders_today = [order for order in orders_lst if order[0].startswith(today)]
    if orders_today:
        print(f"Orders for {today}:")
        for order in orders_today:
            print(f"Order ID: {order[0]}\tCustomer: {order[1]}\tTotal due: ${order[3]:.2f}\tPayment_status: {order[4]}\t Status:{order[5]}")
    else:
        print(f"No orders found for today.")


import os

def load_discounts():
    discounts = {}
    with open("Discounts.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:  # skip empty lines
                continue
            try:
                subtotal, discount = line.split(",")
                discounts[float(subtotal)] = discount
            except ValueError:
                print(f"Invalid line format: {line}")
    return discounts

def print_discounts(discounts):
    print("Current Discount Scheme:")
    print("{:<15}{:<10}".format("Subtotal", "Discount"))
    for subtotal, discount in sorted(discounts.items()):
        print("${:<14}{:<3}%".format(subtotal, discount))

def add_discount(discounts):
    subtotal = float(input("Enter new subtotal: $"))
    if subtotal in discounts:
        print("Error: Subtotal already exists.")
        return
    discount = int(input("Enter discount percentage: "))
    if subtotal <= 50 and discount < 5:
        print("Warning: Discount percentage too low for subtotal.")
    elif subtotal <= 75 and discount < 10:
        print("Warning: Discount percentage too low for subtotal.")
    elif subtotal <= 100 and discount < 15:
        print("Warning: Discount percentage too low for subtotal.")
    elif subtotal > 100 and discount < 20:
        print("Warning: Discount percentage too low for subtotal.")
    elif subtotal <= 0 or discount <= 0:
        print("Error: Invalid input.")
        return
    elif discount > 100:
        print("Error: Discount percentage too high.")
        return
    discounts[subtotal] = discount
    print("Discount added successfully.")
    with open("Discounts.txt", "a") as f:
        f.write(f"{subtotal},{discount}\n")
    print(f"subtotal: {subtotal}, discount: {discount}")
    print(discounts)
    f.close()

def update_discount(discounts):
    subtotal = float(input("Enter existing subtotal to update: $"))
    if subtotal not in discounts:
        print("Error: Subtotal does not exist.")
        return
    new_subtotal = float(input("Enter new subtotal: $"))
    if new_subtotal != subtotal:
        if new_subtotal in discounts:
            print("Error: Subtotal already exists.")
            return
    new_discount = int(input("Enter new discount percentage: "))
    if new_subtotal <= 50 and new_discount < 5:
        print("Warning: Discount percentage too low for subtotal.")
    elif new_subtotal <= 75 and new_discount < 10:
        print("Warning: Discount percentage too low for subtotal.")
    elif new_subtotal <= 100 and new_discount < 15:
        print("Warning: Discount percentage too low for subtotal.")
    elif new_subtotal > 100 and new_discount < 20:
        print("Warning: Discount percentage too low for subtotal.")
    elif new_subtotal <= 0 or new_discount <= 0:
        print("Error: Invalid input.")
        return
    elif new_discount > 100:
        print("Error: Discount percentage too high.")
        return
    del discounts[subtotal]
    discounts[new_subtotal] = new_discount
    print("Discount updated successfully.")
    with open("Discounts.txt", "r") as f:
        lines = f.readlines()
    with open("Discounts.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if float(parts[0]) == subtotal:
                f.write(f"{new_subtotal},{new_discount}\n")
            else:
                f.write(line)
    print(f"subtotal: {new_subtotal}, discount: {new_discount}")
    print(discounts)


def remove_discount(discounts):
    subtotal = float(input("Enter subtotal to remove: $"))
    if subtotal not in discounts:
        print("Error: Subtotal does not exist.")
        return
    del discounts[subtotal]
    print("Discount removed successfully.")
    with open("Discounts.txt", "r") as f:
        lines = f.readlines()
    with open("Discounts.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if float(parts[0]) != subtotal:
                f.write(line)
    print(discounts)




# Display the menu and process user input


while True:
    print()
    print("""
    1.Inventory Management
    2.Sales Management
    3.Discount-Setup
    0.Exit  
    """)
    print()
    option = int(input("Enter a option: "))
    if option == 1:
        print(""""
        -----Inventory Management-----
         a. Bread & Pastry list
         b. Setup new pastry
         c. Update pastry
         d. Re-load pastry from file
         e. Back to main menu
        """)
        sub_choice = input("Enter a choice: ")
        if sub_choice == "a":
            bread_list()
        elif sub_choice == "b":
            setup_list()
        elif sub_choice == "c":
            update_list()
        elif sub_choice == "d":
            reload_pastry()
        elif sub_choice == "e":
            print()
        else:
            print("Invalid option!")
            print()


    elif option == 2:

        while True:
            print("""
        a. Create order
        b. Cancel order
        c. Update order payment
        d. Update order status
        e. List orders (today)
        f: Back to main menu
                """)
            sub_choice = input("Enter a choice: ")
            if sub_choice == "a":
                create_order()
            elif sub_choice == "b":
                cancel_order()
            elif sub_choice == "c":
                update_payment()
            elif sub_choice == "d":
                update_order_status()
            elif sub_choice == "e":
                tdy_lst()
            elif sub_choice == 'f':
                break
            else:
                print("Invalid Option!")

    elif option == 3:
            discounts = load_discounts()
            while True:
                print_discounts(discounts)
                print("\nDiscount Setup Options:")
                print("1. Add new discount")
                print("2. Update existing discount")
                print("3. Remove discount")
                print("0. Return to main menu")

                choice = input("Enter your choice: ")
                if choice == "1":
                    add_discount(discounts)
                elif choice == "2":
                    update_discount(discounts)
                elif choice == "3":
                    remove_discount(discounts)
                elif choice == "0":
                    break
                else:
                    print("Error: Invalid input.")
    elif option == 0:
        print()
        print("Thank You For Using 'SUBS'. Now Exiting. Thank You And Have A Nice Day.")
        exit()
    else:
        print("Invalid option!")





