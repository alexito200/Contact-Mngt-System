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

with open('contact_list.txt', 'w') as file:
    file.write(all_contacts)

print("Contact list saved to 'contact_list.txt'.")
