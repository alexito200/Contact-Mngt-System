contacts = {
    'Alex': {
        'Name': 'Alex',
        'Phone Number': '908-219-9498',
        'Email Address': 'alex200@gmail.com',
        'Adtnl Info': 'This is myself'
    },
    'Vitoria': {
        'Name': 'Vitoria',
        'Phone Number': '908-219-9499',
        'Email Address': 'vitoria200@yahoo.com',
        'Adtnl Info': 'This is my fiancee'
    },
    'Jessica': {
        'Name': 'Jessica',
        'Phone Number': '908-219-9497',
        'Email Address': 'jessica200@live.com',
        'Adtnl Info': 'This is my mom'
    }
}

import re

# Adding new contact
def collect_contact_info():
    name = input("\nEnter the contact's name: ")
    phone = input(f"\nEnter {name}'s phone number (format: '123-456-7890'): ")
    while not re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
        phone = input("\nInvalid phone number. Please enter in '123-456-7890' format: ")
    email = input(f"\nEnter {name}'s email address (format: 'name@email.com'): ")
    while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        email = input("\nInvalid email format. Please enter a valid email (format: 'name@email.com'): ")
    adtnl_info = input(f'\nPlease provide any additional info about {name}: ')
    contacts[name] = {
        'Name': name,
        'Phone Number': phone,
        'Email Address': email,
        'Adtnl Info': adtnl_info
    }
    print(f"Contact '{name}' has been added.")

# Editing existing contact
def edit_contact():
    if not contacts:
        print("\nNo contacts available to edit.")
        return

    dict_edit = input('\nTell me the contact you would like to edit: ')
    
    print("\nAvailable keys for editing:")
    available_keys = contacts[dict_edit].keys()
    for key in available_keys:
        print(f"- {key}")

    dict_key = input('\nProvide a key to access the key-value pair for this contact (e.g., "Name", "Phone Number", "Email Address", "Adtnl Info"): ')

    if dict_key in contacts[dict_edit]:
        dict_value = input(f'\nEnter the new value for "{dict_key}": ')
        contacts[dict_edit][dict_key] = dict_value
        print(f'\nUpdated {dict_edit}\'s {dict_key} to "{dict_value}".')
    else:
        print(f'\nKey "{dict_key}" not found for contact "{dict_edit}".')


# Delete contact
def delete_contact():
    if not contacts:
        print("\nNo contacts available to delete.")
        return

    print("\nAvailable contacts:")
    for index, contact_name in enumerate(contacts, start=1):
        print(f"\n{index}. {contact_name}")

    contact_name = input('\nEnter the name of the contact you would like to delete: ')

    if contact_name in contacts:
        del contacts[contact_name]
        print(f'\nContact "{contact_name}" has been deleted.')
        
        print("\nUpdated contact list:")
        if contacts:
            for index, contact_name in enumerate(contacts, start=1):
                print(f"{index}. {contact_name}")
        else:
            print("No contacts available.")
    else:
        print(f'\nContact "{contact_name}" not found.')


    if contact_name in contacts:
        del contacts[contact_name]
        print(f'\nContact "{contact_name}" has been deleted.')
    else:
        print(f'\nContact "{contact_name}" not found.')


# Search for contact
def search_contact():
    search_contact_name = input('\nTell me the contact that you would like to search for: ')
    
    if search_contact_name in contacts:
        print(contacts[search_contact_name])
    else:
        print('\nThis contact does not exist.')
        print(search_contact_name)

# Display all contacts
def list_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    
    for index, (contact_name, details) in enumerate(contacts.items(), start=1):
        print(f'\nContact #{index}: {details}')

# Export contacts to a text file
def save_contacts_to_file(filename='contact_list.txt'):
    contact_list = []
    for contact_name, details in contacts.items():
        contact_info = (
            f"Name: {details['Name']}\n"
            f"Phone Number: {details['Phone Number']}\n"
            f"Email Address: {details['Email Address']}\n"
            f"Additional Info: {details['Adtnl Info']}\n"
            "--------------------\n"
        )
        contact_list.append(contact_info)

    all_contacts = ''.join(contact_list)

    with open(filename, 'w') as file:
        file.write(all_contacts)

    print(f"Contact list saved to '{filename}'.")

while True:
    print('\nWelcome to the Contact Management System!')
    print('\nMenu:')
    print('\n1. Add a new contact')
    print('\n2. Edit an existing contact')
    print('\n3. Delete a contact')
    print('\n4. Search for a contact')
    print('\n5. Display all contacts')
    print('\n6. Export contacts to a text file')
    print('\n7. Quit')

    user_input = input("\nEnter a number (or 'q' to quit): ").lower()

    if user_input == 'q':
        print("Goodbye!")
        break 

    try:
        user_input = int(user_input)
    except ValueError:
        print("\nInvalid input, please enter a number or 'q' to quit.")
        continue

    if 1 <= user_input <= 6:
        if user_input == 1:
            collect_contact_info()
        elif user_input == 2:
            edit_contact()
        elif user_input == 3:
            delete_contact()
        elif user_input == 4:
            search_contact()
        elif user_input == 5:
            list_contacts()
        elif user_input == 6:
            save_contacts_to_file()
    elif user_input == 7:
        print("Goodbye!")
        break
    else:
        print("\nInvalid option. Please enter a number between 1 and 7.")
