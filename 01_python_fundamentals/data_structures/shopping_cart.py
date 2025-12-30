def menu_options():
    print("\nShopping Cart Menu: ")
    menu_options = ["1. Add item", "2. View Cart",
                    "3. Show total cost", "4. Quit"]
    for option in menu_options:
        print(f"{option}")
    choice = input("Choose: ")
    return choice


# Store items as a list of dict
shopping_cart = []
while True:
    user_choice = menu_options()
    # Menu options (Add items, view cart, show total cost, quit)
    # Adding items to cart
    if user_choice == "1":
        item = input("\nEnter item name: ")
        price = input("\nEnter item price: ")
        price = float(price)
        shopping_cart.append({"name": item, "price": price})
        print("\nItem added!")
    # View cart(fix)
    elif user_choice == "2":
        if not shopping_cart:
            print("No items in cart.")
        else:
            for item in shopping_cart:
                print(f"{item["name"]} - ${item["price"]:.2f}")
    # Total of cart
    elif user_choice == "3":
        if not shopping_cart:
            print("No item in cart.")
        else:
            total = 0
            for item in shopping_cart:
                total += item["price"]
        print(f"Cart Total: ${total:.2f}")
    elif user_choice == "4":
        print("Done!")
        break
    else:
        print("Invalid option.")
