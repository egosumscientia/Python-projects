import json
from collections import namedtuple


class Contact:
    """Represents a contact with a name, phone, and email."""

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def update(self, phone, email):
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"

class ContactManager:
    """Manages a list of contacts and handles operations"""

    def __init__(self):
        self.contacts = []
        self.file = "contacts.json"
        self.load_contacts()

    def add_contact(self, name, phone, email):
        """Adds a new contact"""
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        """Displays all contacts"""
        if not self.contacts:
            print("No contacts available")
            return

        print("\n Contact List: ")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact}")

    def update_contact(self, name):
        """Updates an existing contact"""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone = input("Enter a new phone number: ")
                new_email = input("Enter a new email address: ")
                contact.update(new_phone, new_email)
                self.save_contacts()
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact '{name}' not found")

    def delete_contact(self, name):
        """Deletes a contact"""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

    def save_contacts(self):
        """Saves contacts to a JSON file for persistence"""
        with open(self.file, "w") as f:
            json.dump([contact.__dict__ for contact in self.contacts], f, indent=4)

    def load_contacts(self):
        """Loads contacts from a JSON file when the program starts."""
        try:
            with open(self.file, "r") as f:
                loaded_contacts = json.load(f)
                self.contacts = [Contact(c["name"], c["phone"], c["email"]) for c in loaded_contacts]
        except FileNotFoundError:
            self.contacts = []


def menu():
    """Displays the contact manager menu"""
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu")
        print("1. Add Contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)

        elif option == "2":
            manager.view_contacts()

        elif option == "3":
            name = input("Enter a contact name to update: ")
            manager.update_contact(name)

        elif option == "4":
            name = input("Enter a contact name to delete: ")
            manager.delete_contact(name)

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Wrong option, please try another one.")


#run the program

if __name__ == "__main__":
    menu()






























































