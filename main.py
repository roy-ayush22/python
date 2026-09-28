class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) <self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        marks = 0
        for student in self.students:
            marks += student.get_grade()

        return marks / len(self.students)


s1 = Student("ayush", 21, 81)
s2 = Student("gojo", 28, 98)

course = Course("physics", 2)

course.add_students(s1)
course.add_students(s2)
# print(course.students[0].grade)

print(course.get_average_grade())
