import json
import os

# File to store contacts
FILE_NAME = "phonebook.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)

# Create new contact
def create_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print("Contact added.")

# Read all contacts
def read_contacts(contacts):
    if not contacts:
        print("Phonebook is empty.")
        return
    print("\n--- All Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("Enter new phone number: ").strip()
    contacts[name] = phone
    print("Contact updated.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main app loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ").strip()

        if choice == '1':
            create_contact(contacts)
        elif choice == '2':
            read_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
