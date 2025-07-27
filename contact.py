def contact_list():
    contacts = {}

    while True:
        
        print("1. Add Contact")
        print("2. Look Up Contact")
        print("3. View All Contacts")
        print("4. Remove Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            p_no = input("Enter Phone No: ")
            contacts[name] = p_no
            print(f"Contact for {name} added.")
            
        elif choice == '2':
            name = input("Enter name to look up: ")
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '3':
            
            if not contacts:
                print("Your contact book is empty.")
            else:
                for name, p_no in contacts.items():
                    print(f"{name}: {p_no}")
                print('\n')

        elif choice == '4':
            name = input("Enter name to remove: ")
            if name in contacts:
                contacts.pop(name)
                print(f"Contact for {name} removed.")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '5':
            print("Exiting contact book.")
            break
            
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

contact_list()