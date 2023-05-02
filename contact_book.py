contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
    

while True :
    user_choice = int(input("""1. Add a new contact \n 
    2. Search contact \n 3. Display all contacts \n
    4. Edit contacts \n 5. Delete contact \n
    6. Exit \n Enter your choice?
    
    """ ))
    if user_choice == 1:
        name = input("enter a name? ")
        phone_number = input("enter the mobile number? ")
        contact [name] = phone_number
    elif user_choice == 2:
        search_contact = input("enter the contact name? ")
        if search_contact in contact:
            print(search_contact, "'s contact number is contact[search_contact]")
        else:
            print("Name not found in the contact book")

    elif user_choice == 3:
        if not contact:
            print("An empty contact book")
        else:
            display_contact =()
    elif user_choice ==4:
        edit_contact = input("Enter the contact name to be edited?")
        if edit_contact in contact:
            phone = input("Enter the mobile number?")
            contact[edit_contact]=phone_number
            print("contact_updated")
            display_contact()
        else:
            print("Name not found in the contact book")
    elif user_choice == 5:
        delete_contact = input("Enter the contact to be deleted? ")
        if delete_contact in contact:
            confirm= input("Do you want to delete this contact y/n ")
            if confirm == "y" or confirm =="Y":
                contact.pop(delete_contact)
                display_contact()
        else:
            print("Name not found in the contact book")

    else:
        break        


