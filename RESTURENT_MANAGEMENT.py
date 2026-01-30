# ===== STORE MANAGEMENT SYSTEM =====

# ---- Initial Store Data ----
store_items = {
    1: {"name": "Chicken", "price": 500, "stock": 5},
    2: {"name": "Cold Drink", "price": 100, "stock": 10},
    3: {"name": "Tea", "price": 50, "stock": 8}
}

ADMIN_PASSWORD = "1234"
total_earnings = 0


# ---- Save sales to file ----
def save_sale(text):
    with open("sales_record.txt", "a") as file:
        file.write(text + "\n")


# ---- Customer Mode ----
def customer_mode():
    global total_earnings
    cart_total = 0
    cart_details = []

    while True:
        print("\n*** MENU ***")
        for key, item in store_items.items():
            print(f"{key}. {item['name']} - Rs {item['price']} (Stock: {item['stock']})")
        print("4. Checkout")

        choice = int(input("Enter option: "))

        if choice == 4:
            break

        if choice in store_items:
            item = store_items[choice]
            qty = int(input("Enter quantity: "))

            if qty <= item["stock"]:
                cost = qty * item["price"]
                item["stock"] -= qty
                cart_total += cost
                cart_details.append(f"{item['name']} x{qty} = Rs {cost}")
                print("Added to cart!")
            else:
                print("Out of stock!")
        else:
            print("Invalid choice!")

    # ---- Print Receipt ----
    print("\n===== FINAL BILL =====")
    for line in cart_details:
        print(line)
    print("Total Amount: Rs", cart_total)
    print("======================")

    total_earnings += cart_total
    save_sale(f"SALE: {cart_details} TOTAL: Rs {cart_total}")


# ---- Admin Mode ----
def admin_mode():
    global total_earnings

    password = input("Enter Admin Password: ")
    if password != ADMIN_PASSWORD:
        print("Wrong Password!")
        return

    while True:
        print("\n*** ADMIN PANEL ***")
        print("1. View Stock")
        print("2. Refill Stock")
        print("3. View Total Earnings")
        print("4. Exit Admin")

        choice = int(input("Enter option: "))

        if choice == 1:
            for item in store_items.values():
                print(f"{item['name']} - Stock: {item['stock']}")

        elif choice == 2:
            for key, item in store_items.items():
                print(f"{key}. {item['name']} (Current Stock: {item['stock']})")

            item_id = int(input("Select item to refill: "))
            if item_id in store_items:
                add_qty = int(input("Enter quantity to add: "))
                store_items[item_id]["stock"] += add_qty
                print("Stock Updated!")

        elif choice == 3:
            print("Total Earnings Today: Rs", total_earnings)

        elif choice == 4:
            break

        else:
            print("Invalid option!")


# ---- Main Program ----
while True:
    print("\n===== WELCOME TO THE STORE =====")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    main_choice = int(input("Enter option: "))

    if main_choice == 1:
        customer_mode()

    elif main_choice == 2:
        admin_mode()

    elif main_choice == 3:
        print("Store Closed. Goodbye 🙂")
        break

    else:
        print("Invalid choice!")