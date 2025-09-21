# Password Manager

A secure Password Manager project that helps users safely store and manage their passwords using modern *cybersecurity techniques*.

## Features

- *AES Encryption:* All passwords are encrypted before being saved.
- *Hashed Master Password:* The master password is securely hashed to prevent unauthorized access.
- *Secure Password Storage:* Passwords are stored in a local JSON file (vault.json) with encryption.
- *Random Password Generator:* Generates strong, random passwords to improve security.
- *Modular Code:* main.py handles the main logic, utils.py contains helper functions.

## Cybersecurity Highlights

1. *Encryption:* Uses AES (Advanced Encryption Standard) to encrypt sensitive data.  
2. *Hashing:* The master password is hashed using a secure algorithm to protect against brute-force attacks.  
3. *Data Safety:* Sensitive files like key.key and vault.json are *not pushed to GitHub*.  
4. *Secure Practices:* Only safe source code is tracked in Git, avoiding exposure of real credentials.

## Usage

1. Run main.py to start the Password Manager.  
2. Set a master password (hashed securely).  
3. Add, view, or generate passwords securely.  

