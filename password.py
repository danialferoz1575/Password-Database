import json
import tkinter as tk
from tkinter import messagebox

# Function to load passwords from file
def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save passwords to file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

# Function to add password
def add_password():
    account = account_entry.get()
    password = password_entry.get()

    if not account or not password:
        messagebox.showerror("Error", "Please enter both account and password.")
        return

    passwords = load_passwords()
    passwords[account] = password
    save_passwords(passwords)
    messagebox.showinfo("Success", f"Password for {account} added successfully!")
    list_accounts()

# Function to retrieve password
def get_password():
    account = account_entry.get()

    if not account:
        messagebox.showerror("Error", "Please enter the account.")
        return

    passwords = load_passwords()
    if account in passwords:
        messagebox.showinfo("Password", f"Password for {account}: {passwords[account]}")
    else:
        messagebox.showerror("Error", f"No password found for {account}")

# Function to list accounts
def list_accounts():
    passwords = load_passwords()
    account_list.delete(0, tk.END)
    for account in passwords:
        account_list.insert(tk.END, account)

# Main function
def main():
    # Create main window
    root = tk.Tk()
    root.title("Password Protector")
    root.geometry("400x300")

    # Create labels
    account_label = tk.Label(root, text="Account:", font=("Arial", 12))
    account_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
    password_label = tk.Label(root, text="Password:", font=("Arial", 12))
    password_label.grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)

    # Create entry fields
    global account_entry, password_entry
    account_entry = tk.Entry(root, font=("Arial", 12))
    account_entry.grid(row=0, column=1, padx=20, pady=10, sticky=tk.W+tk.E)
    password_entry = tk.Entry(root, show="*", font=("Arial", 12))
    password_entry.grid(row=1, column=1, padx=20, pady=10, sticky=tk.W+tk.E)

    # Create buttons
    add_button = tk.Button(root, text="Add Password", command=add_password, font=("Arial", 12), bg="#4CAF50", fg="white")
    add_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E)
    get_button = tk.Button(root, text="Get Password", command=get_password, font=("Arial", 12), bg="#FFC107", fg="black")
    get_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E)

    # Create listbox
    global account_list
    account_list = tk.Listbox(root, font=("Arial", 12), width=30)
    account_list.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E)

    # Initial list of accounts
    list_accounts()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
