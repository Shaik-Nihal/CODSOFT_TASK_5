import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox

class ContactBook(QWidget):
    def __init__(self):
        super().__init__()

        self.contacts = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contact Book")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        layout.addWidget(self.name_label)

        self.name_entry = QLineEdit()
        layout.addWidget(self.name_entry)

        self.phone_label = QLabel("Phone Number:")
        layout.addWidget(self.phone_label)

        self.phone_entry = QLineEdit()
        layout.addWidget(self.phone_entry)

        self.email_label = QLabel("Email:")
        layout.addWidget(self.email_label)
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)

        self.address_label = QLabel("Address:")
        layout.addWidget(self.address_label)

        self.address_entry = QLineEdit()
        layout.addWidget(self.address_entry)

        add_button = QPushButton("Add Contact")
        add_button.clicked.connect(self.add_contact)
        layout.addWidget(add_button)

        view_button = QPushButton("View Contact List")
        view_button.clicked.connect(self.view_contacts)
        layout.addWidget(view_button)

        search_button = QPushButton("Search Contact")
        search_button.clicked.connect(self.search_contact)
        layout.addWidget(search_button)

        update_button = QPushButton("Update Contact")
        update_button.clicked.connect(self.update_contact)
        layout.addWidget(update_button)

        delete_button = QPushButton("Delete Contact")
        delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(delete_button)

        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        address = self.address_entry.text()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.name_entry.clear()
            self.phone_entry.clear()
            self.email_entry.clear()
            self.address_entry.clear()
        else:
            QMessageBox.critical(self, "Error", "Please enter name and phone number.")

    def view_contacts(self):
        self.contact_list.clear()
        for name, contact in self.contacts.items():
            item = QListWidgetItem(f"{name} - {contact['phone']}")
            self.contact_list.addItem(item)

    def search_contact(self):
        search_term = self.name_entry.text()
        if search_term:
            for name, contact in self.contacts.items():
                if search_term in name or search_term in contact["phone"]:
                    QMessageBox.information(self, "Search Result", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
                    return
            QMessageBox.information(self, "Search Result", "Contact not found.")
        else:
            QMessageBox.critical(self, "Error", "Please enter search term.")

    def update_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        address = self.address_entry.text()

        if name and phone:
            if name in self.contacts:
                self.contacts[name] = {"phone": phone, "email": email, "address": address}
                self.name_entry.clear()
                self.phone_entry.clear()
                self.email_entry.clear()
                self.address_entry.clear()
            else:
                QMessageBox.critical(self, "Error", "Contact not found.")
        else:
            QMessageBox.critical(self, "Error", "Please enter name and phone number.")

    def delete_contact(self):
        name = self.name_entry.text()
        if name:
            if name in self.contacts:
                del self.contacts[name]
                self.name_entry.clear()
                self.phone_entry.clear()
                self.email_entry.clear()
                self.address_entry.clear()
            else:
                QMessageBox.critical(self, "Error", "Contact not found.")
        else:
            QMessageBox.critical(self, "Error", "Please enter name.")

def main():
    app = QApplication(sys.argv)
    contact_book = ContactBook()
    contact_book.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()