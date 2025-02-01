import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)

    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name} - {details['Phone']}")

# Search contact by name or phone
def search_contact():
    contacts = load_contacts()
    query = input("Enter name or phone number to search: ")

    for name, details in contacts.items():
        if query == name or query == details["Phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            return
    print("Contact not found.")

# Update a contact
def update_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print("\nEnter new details (leave blank to keep existing data):")
        phone = input(f"New phone number ({contacts[name]['Phone']}): ") or contacts[name]["Phone"]
        email = input(f"New email ({contacts[name]['Email']}): ") or contacts[name]["Email"]
        address = input(f"New address ({contacts[name]['Address']}): ") or contacts[name]["Address"]

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)

        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
def contact_book():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the contact book
contact_book()
