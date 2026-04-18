#Sharath lives in Chennai - 600001
class Address:
    def __init__(self, city:str, pincode:int):
        self.city = city
        self.pincode = pincode

    
class user(Address):
    def __init__(self, name:str, city:str, pincode:int):
        self.name = name
        super().__init__(city,pincode)

    def display_user_Address(self):
        print(f"{self.name} lives in {self.city} - {self.pincode}")

sharath = user("sharath", "Chennai", 600001)
sharath.display_user_Address()