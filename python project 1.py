# Simple account login/create program
import os

a = None  # stored account number (string)
b = None  # stored password (string)
Name = None
Age = None
gender = None
I = 1000

# Load account if exists
try:
    with open("account.txt","r") as f:
        data = [s.strip() for s in f.read().split(",")]
        if len(data) >= 2 and data[0] and data[1]:
            a = data[0]
            b = data[1]
            if len(data) >= 3:
                Name = data[2]
            if len(data) >= 4:
                Age = data[3]
            if len(data) >= 5:
                gender = data[4]
except FileNotFoundError:
    pass

logged_in = False
current_account = None

while True:
    print("Login Menu")
    try:
        x = int(input("Enter 0 to login, Enter 1 to create new account, Enter 2 to exit: "))
    except ValueError:
        print("Invalid input. Enter 0, 1 or 2.")
        continue

    if x == 0:
        if a is None:
            print("No account found. Please create an account first.")
            continue
        max_attempts = 3
        attempts = 0
        success = False
        while attempts < max_attempts:
            A = input("Enter the account number: ")
            B = input("Enter the password: ")
            if A == a and B == b:
                print("Login successful ")
                print("Account:", A)
                success = True
                logged_in = True
                current_account = A
                break
            else:
                attempts += 1
                print(f"Invalid (attempt {attempts}/{max_attempts})")
        if success:
            break
        else:
            print("Too many failed login attempts. Returning to menu.")

    elif x == 1:
        print("Create new account")
        Name = input("Enter your name : ")
        Age = input("Enter your age : ")
        gender = input("Enter your gender: ")
        accountnumber = input("Enter your account number: ")
        password = input("Enter new password: ")
        password_ = input("Enter the password again: ")

        if password == password_:
            a = accountnumber.strip()
            b = password
            with open("account.txt", "w") as f:
                f.write(f"{accountnumber},{password},{Name},{Age},{gender}")
            print("Account created successfully")
            print("Please login now")
            continue
        else:
            print("Password incorrect")

    elif x == 2:
        print("Exiting program")
        break

    else:
        print("Invalid choice, try again")

# after login menu
if logged_in:
    I = 1000
    print("Name", Name)
    print("Age", Age)
    print("Gender", gender)
    print("Your account number is", current_account)
    print("Your account balance is", I)
    signout_ = input("To Logout enter 9: ")
    if signout_ == "9":
        print("Logged out successfully")
else:
    print("No successful login. Program ended.")
