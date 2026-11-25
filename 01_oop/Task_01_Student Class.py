
class Student:
    university: str = "KFSU"
    student_count: int = 0

    def __init__(self, name: str, age: int,
                 student_id: int, gpa: float) -> None:
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

        Student.student_count += 1

    def display_info(self) -> None:
        print("Student Information".center(50, "*"))
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.student_id}")
        print(f"GPA: {self.gpa}")
        print("*" * 50)

    def is_honor_student(self) -> bool:
        return self.gpa >= 3.5

    def update_gpa(self, new_gpa: float) -> None:
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
        else:
            print("Invalid GPA!")

    @classmethod
    def change_university(cls, new_university: str) -> None:
        cls.university = new_university

    @classmethod
    def display_university(cls) -> None:
        print(f"University: {cls.university}")

    @classmethod
    def display_student_count(cls) -> None:
        print(f"Number of Students: {cls.student_count}")


# Creating Students
student1 = Student("Alia", 18, 1, 3.4)
student2 = Student("Hala", 18, 2, 3.2)
student3 = Student("Sara", 18, 3, 3.8)


# Student Count
print("\n" + "=" * 50)
print("STUDENT COUNT")
print("=" * 50)
Student.display_student_count()


# Display Student Information
print("\n" + "=" * 50)
print("STUDENT DETAILS")
print("=" * 50)

student1.display_info()

# Check Honor Status
print("Honor Status:",
      "Great Student" if student1.is_honor_student()
      else "Try harder")


# Update GPA
print("\n" + "=" * 50)
print("UPDATING GPA")
print("=" * 50)

student1.update_gpa(3.7)
print(f"New GPA: {student1.gpa}")

print("Honor Status:",
      "Great Student" if student1.is_honor_student()
      else "Try harder")


# Display Current University
print("\n" + "=" * 50)
print("UNIVERSITY")
print("=" * 50)

student1.display_university()


# Change University for All Students
print("\nChanging university...")
Student.change_university("Cairo University")

print("\nUniversity after changing:")
student1.display_university()
student2.display_university()
student3.display_university()


# Change University for One Object Only
print("\n" + "=" * 50)
print("INSTANCE ATTRIBUTE TEST")
print("=" * 50)

student1.university = "Alexandria University"

print("Student 1:", student1.university)
print("Student 2:", student2.university)
print("Student 3:", student3.university)
print("Class University:", Student.university)
