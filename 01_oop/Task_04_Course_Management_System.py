class Course:
    university: str = "KFSU"
    total_courses: int = 0
    
    def __init__(self,
    course_name:str,
    course_code:str)->None:
        self.course_name=course_name
        self.course_code=course_code
        self.students: list[str] = []
        self.grades: dict[str,float] = {}

        Course.total_courses+=1

    @classmethod
    def change_university(cls,new_uni_name:str)->None:
        cls.university=new_uni_name

    @staticmethod
    def is_valid_grade(grade:float)->bool:
        return 0<=grade<=100

    def add_student(self,student_name:str)->None:
        self.students.append(student_name)

    def remove_student(self,student_name:str)->None:
        if student_name in self.students:
            self.students.remove(student_name)
            self.grades.pop(student_name,None)
        
        else:
            raise ValueError("Student is not enrolled in this course!")

    def add_grade(self,student_name:str,grade:float)->None:
        if Course.is_valid_grade(grade) and student_name in self.students:
            self.grades[student_name]=grade 
        else:
            raise ValueError("Enter a valid grade!")

    def get_student_grade(self,student_name:str)-> float|None:
        return self.grades.get(student_name)

# Create Course objects
course1 = Course("Python", "CS101")
course2 = Course("Machine Learning", "AI201")

# Add students
course1.add_student("Ali")
course1.add_student("Sara")
course2.add_student("Ali")
course2.add_student("Omar")

# Add grades
course1.add_grade("Ali", 95.5)
course1.add_grade("Sara", 0.0)
course2.add_grade("Ali", 88.0)

# Display course information
print(course1.course_name)
print(course1.students)
print(course1.grades)

# Get student grades
print(course1.get_student_grade("Ali"))
print(course1.get_student_grade("Sara"))
print(course1.get_student_grade("Omar"))

# Test static method without an object
print(Course.is_valid_grade(90))
print(Course.is_valid_grade(120))

# Change university
Course.change_university("New University")

# Test class attributes
print(course1.university)
print(course2.university)
print(Course.total_courses)


