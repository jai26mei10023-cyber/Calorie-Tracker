# auth.py
import hashlib
from config import USERS_FILE
from storage import load_json, save_json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = load_json(USERS_FILE)
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists.")
        return None
    password = input("Enter a password: ")
    users[username] = hash_password(password)
    save_json(USERS_FILE, users)
    print("Registration successful.")
    return username

def login():
    users = load_json(USERS_FILE)
    print("\n--- Login ---")
    username = input("Enter username: ")
    if username not in users:
        print("User not found.")
        return None
    password = input("Enter password: ")
    if users[username] == hash_password(password):
        print("Login successful.")
        return username
    else:
        print("Incorrect password.")
        return None