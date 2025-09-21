from utils import generate_key, encrypt_password, decrypt_password
import json
import os
import getpass

vault_file = "vault.json"

# --- Optional: Master Password ---
MASTER_PASSWORD = "dharshana"  # Change this to your own secure password

pw = getpass.getpass("Enter master password: ")
if pw != MASTER_PASSWORD:
    print("Incorrect password. Exiting.")
    exit()

# Generate encryption key if it doesn't exist
if not os.path.exists("key.key"):
    generate_key()

# --- Vault Operations ---
def save_password(service, password):
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        vault = {}

    vault[service] = encrypt_password(password)

    with open(vault_file, "w") as f:
        json.dump(vault, f)
    print(f"Password for {service} saved successfully!")

def get_password(service):
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        return None

    encrypted = vault.get(service)
    if encrypted:
        return decrypt_password(encrypted)
    else:
        return None

def list_services():
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        print("No passwords saved yet.")
        return
    if vault:
        print("Saved services:")
        for service in vault.keys():
            print("-", service)
    else:
        print("No passwords saved yet.")

def delete_password(service):
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        print("Vault is empty.")
        return

    if service in vault:
        del vault[service]
        with open(vault_file, "w") as f:
            json.dump(vault, f)
        print(f"{service} deleted successfully!")
    else:
        print("Service not found.")

# --- Main CLI Loop ---
while True:
    print("\nPassword Manager") 
    print("1: Save password")
    print("2: Get password")
    print("3: Exit")
    print("4: List all services")
    print("5: Delete a password")
    choice = input("Enter choice: ")

    if choice == "1":
        service = input("Service name: ")
        password = getpass.getpass("Password: ")
        save_password(service, password)
    elif choice == "2":
        service = input("Service name: ")
        password = get_password(service)
        if password:
            print(f"Password for {service}: {password}")
        else:
            print("Service not found!")
    elif choice == "3":
        break
    elif choice == "4":
        list_services()
    elif choice == "5":
        service = input("Service name to delete: ")
        delete_password(service)
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
    cont=input("Do you want to continue?(y/n): ").lower()
    if cont!="y":
        print("Thank you!")
        break
