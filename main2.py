from utils import generate_key, encrypt_password, decrypt_password
import json
import os
import getpass

vault_file = "vault.json"

# Master password
MASTER_PASSWORD = "mypassword123"
pw = getpass.getpass("Enter master password: ")
if pw != MASTER_PASSWORD:
    print("Incorrect password. Exiting.")
    exit()

# Generate key if it doesn't exist
if not os.path.exists("key.key"):
    generate_key()

# Vault operations
def save_password():
    service = input("Service name: ")
    password = getpass.getpass("Password: ")
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        vault = {}
    vault[service] = encrypt_password(password)
    with open(vault_file, "w") as f:
        json.dump(vault, f)
    print(f"Password for {service} saved successfully!")

def get_password():
    service = input("Service name: ")
    try:
        with open(vault_file, "r") as f:
            vault = json.load(f)
    except FileNotFoundError:
        print("Vault is empty.")
        return
    encrypted = vault.get(service)
    if encrypted:
        print(f"Password for {service}: {decrypt_password(encrypted)}")
    else:
        print("Service not found!")

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

def delete_password():
    service = input("Service name to delete: ")
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

# Step-by-step flow
while True:
    print("\nChoose an action:")
    print("1: Save password")
    print("2: Get password")
    print("3: List all services")
    print("4: Delete a password")
    action = input("Enter choice (1-4): ")

    if action == "1":
        save_password()
    elif action == "2":
        get_password()
    elif action == "3":
        list_services()
    elif action == "4":
        delete_password()
    else:
        print("Invalid choice!")

    cont = input("\nDo you want to continue? (y/n): ").lower()
    if cont != "y":
        print("Exiting Password Manager. Goodbye!")
        break
