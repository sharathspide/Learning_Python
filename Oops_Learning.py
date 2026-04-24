class person:
    def __init__(self, name: str, age: int, email: str, phone_number: int):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def email_validation(self):
        email = self.email
        email_context = email.split("@")
        isGmail = email_context[1]
        if isGmail:
            return True
        else:
            return False
        
    def displayPersonDetails(self):
        context = f"{self.name} is currently {self.age} years old. Inorder to contact {self.name}, for email: {self.email} and for voice chat: {self.phone_number}"
        return context
    

class student(person):
    def __init__(self, name: str, age: int, email: str, phone_number: int, rollNumber: int, standard: str, school: str):
        super().__init__(name, age, email, phone_number)
        self.rollNumber = rollNumber
        self.standard = standard
        self.school = school

    def display_Student_Detail(self):
        print(f"{self.name} is currently a student who's roll number is {self.rollNumber} from the school {self.school} in the class {self.standard}\n student contact details include email: {self.email} and Phone number: {self.phone_number}")


sharath = person("sharath", 27, "rasharath619@gmail.com", 8825575005)
isValiEmail = sharath.email_validation()
if isValiEmail:
    print("The Email for the person is validated")

else:
    print("Wrong email. Validation failed")

print(sharath.displayPersonDetails())

# vasanth = person("vasanth", 27, "vasanth@gmail.com", 8825575005)
vasanth = student("vasanth", 27, "vasanth@gmail.com", 8825575005, 463, "5th standard", "SBOA-Matric HR. SEC. School")

vasanth.display_Student_Detail()