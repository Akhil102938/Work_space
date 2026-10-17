class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average_marks(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        return average

    def display(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll No.:", self.roll_no)

        for i, mark in enumerate(self.marks, start=1):
            print(f"Subject {i}: {mark}")

        print("Total Marks:", sum(self.marks))
        print("Average Marks:", self.average_marks())

    def result(self):
        print("Result:")
        if all(mark >= 35 for mark in self.marks):
            print("PASS 🎉")
        else:
            print("FAIL")


name = input("Enter Student Name: ")
roll_no = int(input("Enter Student Roll No.: "))

marks = []

for i in range(1, 4):
    while True:
        mark = int(input(f"Enter marks for Subject {i} (0-100): "))

        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

s1 = Student(name, roll_no, marks)

s1.display()
s1.result()
