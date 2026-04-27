class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.subjects = {}  # dictionary → {subject: marks}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def total_marks(self):
        return sum(self.subjects.values())

    def print_report_card(self):
        print(f"\n===== REPORT CARD =====")
        print(f"Name       : {self.name}") #This is called an f-string (formatted string literal).
        print(f"Student ID : {self.student_id}") # An f-string is a string where you can directly embed variables or expressions inside {}.
        print("----------------------")
"""
Why the f?

The f before quotes tells Python:

“Evaluate anything inside {} and insert its value here.”

Without f, it’s just a normal string
"""
        for subject, marks in self.subjects.items():
            print(f"{subject:<10} : {marks}")

        print("----------------------")
        print(f"Total Marks: {self.total_marks()}")
        print("======================\n")


# ---- Usage ----
s1 = Student("Kiran", 101)

s1.add_subject("Math", 90)
s1.add_subject("Science", 85)
s1.add_subject("English", 88)

s1.print_report_card()