'''
Simple E-Commerce User System

Create:

Base Class:
User
- name
- email
- method: login()

Child Classes:
Customer
- method: place_order()

Admin
- method: manage_products()

Add Polymorphism:
Override login() differently for Admin & Customer

'''


class User:
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        self.isLoggedIn = False
        self.isAdmin = False

    def login(self):
        self.isLoggedIn = True
        email = self.email
        split_email = email.split("@")
        if split_email[1] == "gmail.com":
            self.isAdmin = False
        else:
            self.isAdmin = True

        if self.isAdmin:
            print ("Admin logged in")
        else:
            print("login successful!!")

class Customer(User):
    def __init__(self, name:str, email:str):
        super().__init__(name, email)

    def place_order(self):
        print("validating the customer login status...")
        self.login()
        if self.isAdmin:
            print("you do not have access to the place order")
        else:
            print("Order Placed SuccessFully")

class Admin(User):
    def __init__(self, name:str, email:str):
        super().__init__(name, email)

    def manage_products(self, productName:str, productQuantity: int):
        print("validating the admin login status...")
        self.login()
        if self.isAdmin:
            print(f"Qantity of {productQuantity} is added against the {productName} in the Data Base")
        else:
            print("you do not have access to the manage inventory")


def customerORadminValidation(useremail):
    email = useremail
    split_email = email.split("@")
    if split_email[1] == "gmail.com":
        print(split_email[1])
        return True
    else:
        print(split_email[1])
        return False

username = input("Enter your name: ")
useremail = input("Enter your email address: ")

if customerORadminValidation(useremail):
    user = Customer(username, useremail)
    user.place_order()

else:
    user = Admin(username, useremail)
    user.manage_products("Jetty", 10)

# users = [Customer(username, useremail),Admin(username, useremail)]

# for user in users:
#     user.login()