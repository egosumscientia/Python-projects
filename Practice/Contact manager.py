import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from a JSON file."""
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Saves contacts to a JSON file"""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts, name, phone, email):
    """Adds a new contact"""
    contacts.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip()})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Displays all contacts"""
    if not contacts:
        print("No contacts available")
        return

    print("\n Contact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

def update_contact(contacts, name):
    """Updates an existing contact"""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter a new phone number: ").strip()
            new_email = input("Enter a new email address: ").strip()
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully!")
            return
    print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    """Deletes a contact"""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{name}' deleted successfully")
            return
    print(f"Contact '{name}' not found. ")


def menu():
    """Displays the menu for the contact manager. """
    contacts = load_contacts()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(contacts, name, phone, email)

        elif option == "2":
            view_contacts(contacts)

        elif option == "3":
            name = input("Enter the contact name to update: ")
            update_contact(contacts, name)

        elif option == "4":
            name = input("Enter a contact name to delete")
            delete_contact(contacts, name)

        elif option == "5":
            print("Goodbye!")
            return

        else:
            print("Wrong option, please try another one")

#Run the program
if __name__ == "__main__":
    menu()