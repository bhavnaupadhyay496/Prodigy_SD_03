import os

CONTACTS_FILE = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    contacts.append({"name": parts[0], "phone": parts[1], "email": parts[2]})
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
    print("Contacts saved successfully.")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            name = input(f"Enter new name (leave blank to keep '{contact['name']}'): ")
            phone = input(f"Enter new phone (leave blank to keep '{contact['phone']}'): ")
            email = input(f"Enter new email (leave blank to keep '{contact['email']}'): ")

            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email

            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Deleted contact: {deleted['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
