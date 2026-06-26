
n = int(input("How many numbers u want to add ="))
contacts = []
for i in range(n):
    print("\nContact", i+1)
    name = input("Enter Name:")
    phone = int(input("Enter Contact Number ="))
    email = input("Enter email =")

    contact = {
        "name":name,
        "phone":phone,
        "email": email
    }
    contacts.append (contact)
print("\n All Contacts")
for contact in contacts:
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print()
#search contact
found = False
search_name = input("\nEnter name to search =")
for contact in contacts:
    if contact["name"]== search_name:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        found = True
        
if not found:
    print("contact not found")
#delete 
found = False
delete_name = input("\nEnter name to delete =")
for contact in contacts:
    if contact["name"] == delete_name:
        contacts.remove(contact)
        print("Contact deleted successfully")
        found = True

if not found:
    print("Contact not found")
#update
found = False
update_name = input("\nEnter Name to update =")
for contact in contacts:
    if contact["name"] == update_name:
        new_phone = int(input("Enter new phone = "))
        new_email = input("Enter new email = ")
        contact["phone"]=new_phone
        contact["email"] = new_email
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Data updated Successfully")
        found = True

if not found:
    print("Contact not found")

print("\nUpdated Contacts")
for contact in contacts:
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        name = input("Enter Name = ")
        phone = int(input("Enter Phone Number = "))
        email = input("Enter Email = ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact Added Successfully")

    elif choice == 2:
        print("\nAll Contacts")
        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print()

    elif choice == 3:
        found = False
        search_name = input("Enter name to search = ")

        for contact in contacts:
            if contact["name"] == search_name:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("Contact not found")

    elif choice == 4:
        found = False
        delete_name = input("Enter name to delete = ")

        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Contact deleted successfully")
                found = True

        if not found:
            print("Contact not found")

    elif choice == 5:
        found = False
        update_name = input("Enter name to update = ")

        for contact in contacts:
            if contact["name"] == update_name:
                new_phone = int(input("Enter new phone = "))
                new_email = input("Enter new email = ")

                contact["phone"] = new_phone
                contact["email"] = new_email

                print("Data updated successfully")
                found = True

        if not found:
            print("Contact not found")

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")

  

        

