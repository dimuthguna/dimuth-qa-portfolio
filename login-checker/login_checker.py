# Simple Login Checker
# Simulates a login system with a limited number of attempts

VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"
MAX_ATTEMPTS = 3

def check_login(username, password):
    return username == VALID_USERNAME and password == VALID_PASSWORD

def main():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if check_login(username, password):
            print("Login successful! Welcome,", username)
            return
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Invalid credentials. {remaining} attempt(s) remaining.")
            else:
                print("Login failed. Maximum attempts exceeded.")

if __name__ == "__main__":
    main()
