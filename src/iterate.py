class Student:
    def __init__(self, name, grade):
        self.name = name    # Object state
        self.grade = grade  # Object state
        self.present = True

# 1. Create a list containing instances of the class
classroom = [Student("Alice", "A"), Student("Bob", "B")]

# 2. Iterate and read the state of each object
for student in classroom:
    print(f"{student.name} has a grade of {student.grade}")
