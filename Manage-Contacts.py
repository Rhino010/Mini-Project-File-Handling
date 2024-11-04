# 1. Write out main function with printed choices
# 2. Write out mock dictionary of keys and values for conttacts to understand base set up
# 3. Create each function needed for each selectable choice from the menu
# 4. Code out each function one by one.
# 5. Create '.txt' files to draw info or add info to
# 6. Add extra features that would make the UI cleaner

# importing 'os' module to use the clear feature for a cleaner UI
import os
import json

# Add contact function to create new users and add to the dictionary
def add_contact(contact_dict):
    email = input("Please enter contact's email. *Note*: this will also be the access key when attempting to search for this contact:\n")
    name = input("Please enter the contact's name:\n")
    phone_number = input("Enter contact's phone number as (xxx-xxx-xxxx):\n")
    notes = input("Enter anything of note for this contact:\n")

    contact_dict[email] = { 'name': name,
                            'phone_number': phone_number,
                            'email': email,
                            'notes': notes
                            }

# Edit user function. When email is changed the old iteration is deleted and a new one is created to use the new email as the key
def edit_contact(contact_dict):
    contact_dict_key = input("Please enter the email of the contact you wish to edit:\n")
    info_key = input("What would you like to update? Please type(name/phone number/email/notes)\n")
    if info_key == 'name':
        name = input("What would you like to replace the contact's name with?\n")
        contact_dict[contact_dict_key]['name'] = name
    elif info_key == 'phone number':
        phone_number = input("What is the new phone number? Be sure to enter phone number as (xxx-xxx-xxxx\n")
        contact_dict[contact_dict_key]['phone_number'] = phone_number
    elif info_key == 'email':
        new_email = input('Please enter the new email for this account. The account key will be changed to this new email as well.\n')
        contact_dict[new_email] = contact_dict[contact_dict_key]
        contact_dict[new_email]['name'] = contact_dict[contact_dict_key]['name']
        contact_dict[new_email]['phone_number'] = contact_dict[contact_dict_key]['phone_number']
        contact_dict[new_email]['notes'] = contact_dict[contact_dict_key]['notes']
        contact_dict[new_email]['email'] = new_email
        contact_dict.pop(contact_dict_key) 
    elif info_key == 'notes':
        notes = input("What notes would you like to add to this account?")
        contact_dict[contact_dict_key]['notes'] = notes
    else:
        print('Not a valid response. Back to main menu.')

# Delete user function. Used .pop() to remove user based off email.
def delete_contact(contact_dict):
    email = input('What is the email of the contact you would like to delete?\n')
    contact_dict.pop(email)

# Able to find specific user through the email. 
def find_contact(contact_dict):
    email = input('What is the email of the contact you would like to delete?\n')
    print("\nUser found. Here are the details.\n\n")
    print(f'User: {contact_dict[email]['email']}\n\tName: {contact_dict[email]['name']}\n\tPhone Number: {contact_dict[email]['phone_number']}\n\tEmail: {contact_dict[email]['email']}\n\tNotes: {contact_dict[email]['notes']}')

# Hard coded more readable layout when displaying all contacts.
def display_contacts(contact_dict):
    for contact, info in contact_dict.items():
        print(f"\nUser Account: {contact_dict[contact]['email']}\n")
        for key, value in info.items():
            print(f"\t{key}: {value}")

# Exports information to 'contacts.txt'. Hard coded the dictionary layout for increased readability. An easier way would be to use the json module .dumps() method, but wanted to stay consistent with the lesson.
def export_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for user, info in contacts.items():
            file.write(f"{user},{info['name']},{info['phone_number']},{info['notes']}\n")
    print("Contacts exported to contacts.txt successfully.")


def import_contacts(filename,contacts):
    with open(filename, 'r') as file:
        for line in file:
            email,name,phone_number,notes = line.strip().split(',')
            contacts[email] = {"name":name, "phone_number": phone_number, "notes": notes, "email": email}
    print("Contacts imported successfully.")


def main():

    contact_dict = {}

    export_import_file = 'contacts.txt'

    while True:
        print("\n1. Add a Contact\n2. Edit Existing Contact\n3. Delete Contact\n4. Search for Contact\n5. Display all Contacts\n6. Export Contacts\n7. Import Contacts\n8. Close Program ")
        choice = input("Please make your selection.\n")

        if choice == '1':
            os.system('cls||clear')
            add_contact(contact_dict)
        elif choice == '2':
            os.system('cls||clear')
            edit_contact(contact_dict)
        elif choice == '3':
            os.system('cls||clear')
            delete_contact(contact_dict)
        elif choice == '4':
            os.system('cls||clear')
            find_contact(contact_dict)
        elif choice == '5':
            os.system('cls||clear')
            display_contacts(contact_dict)
        elif choice == '6':
            os.system('cls||clear')
            export_contacts(export_import_file, contact_dict)
        elif choice == '7':
            os.system('cls||clear')
            import_contacts(export_import_file, contact_dict)
        elif choice == '8':
            os.system('cls||clear')
            print('Program closed. Thank you for using the Contact Management System.')
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()