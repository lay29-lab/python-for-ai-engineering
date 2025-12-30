# List menu options out
def menu_options():
    print("\nContact Book Menu: ")
    menu_options = ["1. Add contact", "2. View all contacts",
                    "3. Search for contact by name", "4. Quit"]
    for option in menu_options:
        print(f"{option}")
    choice = input("Choose: ")
    return choice


contact_book = {}
while True:
    # store contacts as {name: phone_number}
    menu_choice = menu_options()

    # Adding contacts
    if menu_choice == "1":
        name = input("Name: ")
        phone = input("Phone Number: ")
        if name in contact_book:
            print("Contact already exists.")
        else:
            contact_book[name] = phone
            print("\nContact added!")
    # View contacts
    elif menu_choice == "2":
        if not contact_book:
            print("\nNo contacts stored.")
        else:
            for name, phone in contact_book.items():
                print(f"\n{name}: {phone}")
    # Searching contacts by name
    elif menu_choice == "3":
        if not contact_book:
            print("\nNo contacts stored.")
        else:
            search_name = input("\nSearch Name: ")
            if search_name in contact_book:
                print(f"\n{search_name}: {contact_book[search_name]}")
            else:
                print("\nContact not found.")
    elif menu_choice == "4":
        print("Done!")
        break
    else:
        print("Invalid option.")
