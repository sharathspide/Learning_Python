class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.salary = kwargs.get("salary")
        self.department = kwargs.get("department")
        self.isBonus_given = False

    def calculate_bonus(self,give_bonus:bool):
        bonus = 0
        self.isBonus_given = give_bonus
        if(give_bonus):
            bonus = int((self.salary*10)/100)
        self.bonus = bonus

    def display_salary(self):
        if (self.isBonus_given):
            print(f"The Salary of the Employee is {self.salary+self.bonus}")
        else:
            print(f"The Salary of the Employee is {self.salary}")


sharath_data = {
    "name":"Sharath",
    "salary":10000,
    "department":"GEV-Developer"
    }
    
vasanth_data = {
    "name":"vasanth",
    "salary":10000,
    "department":"GEV-Developer"
    }

sharath = Employee(**sharath_data)
sharath.calculate_bonus(True)
sharath.display_salary()
vasanth = Employee(**vasanth_data)
vasanth.calculate_bonus(False)
vasanth.display_salary()
# sharath = Employee("Sharath", 10000, "GEV-Developer")
# ram = Employee("Ram", 10000, "GEV-Developer")
# vasanth = Employee("Vasanth", 10000, "GEV-Developer")


# sharath.calculate_bonus(True)
# sharath.display_salary()
# sharath.calculate_bonus(False)
# vasanth.display_salary()
# ram.calculate_bonus(True)
# ram.display_salary()