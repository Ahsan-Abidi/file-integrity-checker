import json
import bcrypt
import os

USER_FILE = "users.json"


def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


# ---------------- SIGNUP ----------------
def signup(username, password):
    users = load_users()

    # check if user exists
    for user in users:
        if user["username"] == username:
            return False, "User already exists"

    # hash password
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users.append({
        "username": username,
        "password": hashed.decode()
    })

    save_users(users)
    return True, "Signup successful"


# ---------------- LOGIN ----------------
def login(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return True
            else:
                return False

    return False