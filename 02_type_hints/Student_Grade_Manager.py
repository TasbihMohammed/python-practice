students: dict[str, float] = {
    "Ahmed": 85,
    "Sara": 92,
    "Omar": 45,
    "Mona": 76
}
course_name:str="Python"
passing_grade:float = 50.0

def add_student(name:str,grade:float)->None:
    students[name]=grade

def get_grade(name:str)->float|None:
    return students.get(name)

def calculate_average()->float:
    grades=students.values()
    if not students:
        raise ZeroDivisionError("No grades to calculate")
    return sum(grades)/len(grades)

def get_passed_students()->list[str]:
    passed_students=[]
    for name,grade in students.items():
        if grade>=passing_grade:
            passed_students.append(name)
    return passed_students

def display_report()->None:
    print(f"Course name: {course_name}")
    for student in students.items():
        print(f"Student name: {student[0]}, grade: {student[1]}")

    print("Average grade: ",calculate_average())

def find_top_student()->str|None:
    if not students:
        return None   
    return max(students, key=students.get)



