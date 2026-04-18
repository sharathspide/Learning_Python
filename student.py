class student:
    def __init__(self,name:str, marks:int):
        self.name = name
        self.marks = marks

    def display_student_details(self):
        print(f"Student Name is {self.name} and I have a scored {self.marks}%")

sharath = student("Sharath",98)
ram = student("Ram",97)
vasanth = student("vasanth",99)
saravanan = student("Saravanan",99)

sharath.display_student_details()
ram.display_student_details()
vasanth.display_student_details()
saravanan.display_student_details()