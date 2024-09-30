Contact Management System by Alex Alarcon

TOC:
1. Adding New Contact
2. Editing existing contact
3. Deleting contact
4. Searching for contact
5. Displaying all contacts
6. Exporting contacts to a text file
7. Quitting


1. To add a new contact, the user inputs '1' into the main menu. The program then prompts the user to enter the contact's name, the phone number, email, and any other additional info.
   For each of those prompts, the program uses regex validation to make sure the input is in the correct format. Once all of the contact's information is entered and
   in the correct format, the program returns a 'Contact {name} has been added.'

2. To edit an existing contact, the user inputs '2' into the main menu. The program then prompts the user to enter the name of the contact they would like to edit. The program assists
   the user by showing them the possible keys to enter. Then, it asks for the key-value pair they would like to edit. Finally, the program will show a message that the key-value
   selected has been updated.

3. To delete a contact, the user inputs '3' into the main menu. The program will list out all of the available contacts to delete to make it easier for the user to choose.
   Once an appropriate selection has been made, the program will print a message that the contact has been deleted as well as print out the update list of contacts.

4. To search for a contact, the user inputs '4' into the main menu. The program will ask for the contact's name. Once the appropriate selection has been entered, the program will
   print out the contact's info.

5. To display all contacts, the user inputs '5' into the main menu. The program will then print out all of the contacts stored in the 'Contacts' dictionary. The program will take
   into account the contacts that have been deleted when displaying the list.

6. To export all contacts to a text file, the user inputs '6' into the main menu. The program then runs a function called 'save_contacts_to_file'. This function converts the contacts
   dictionary into a list first and exports that list into a newly created file called 'contact_list.txt'. The list will appear in a user-friendly format for better readability.

7. To quit the program, the user has two options, to input either '7' or 'q'. Both inputs will quit the program.
