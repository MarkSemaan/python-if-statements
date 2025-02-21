
Username = "admin"
Password = "1234"

loginName = input("Enter Username: ")
loginPass = input("Enter Password: ")

if loginName == Username and loginPass == Password:
    print("Access granted.")
else:
    print("Access denied.")