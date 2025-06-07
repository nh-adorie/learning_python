# Create a Class named Student with
# Attributes: name, age, grade
# Method: display_info(), is_passed()

# Then, create 2 object from Student class
# Call display_info() and is_passed()


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Student Name: {self.name}\nStudent Age: {self.age}\nStudent Grade: {self.grade}")

    def is_passed(self):
        if self.grade >= 5:
            print("Passed")
        else:
            print("Failed")
    
    def add_bonus(self,bonus):
        self.grade += bonus
        if self.grade > 10:        
            self.grade = 10

student_info = {
    "adorie" : {
       "age": 22,
       "grade": 4, 
    },
    "foxie": {
        "age": 23,
        "grade": 7
    },
}

students = []

for name, info in student_info.items():
    student = Student(name,info["age"],info["grade"])
    students.append(student)

for student in students:
    student.display_info()