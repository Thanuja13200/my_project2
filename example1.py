class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Thanuja", 90)
s2 = Student("Alice", 85)

s1.display()
s2.display()