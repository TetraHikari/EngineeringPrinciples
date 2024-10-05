class University:
    def __init__(self, name):
        self.name = name
        self.student_map = {}
        self.program_map = {}

    def add_student(self, student):
        self.student_map[student.id] = student

#University owns the Program
class Program:
    def __init__(self, name, level, start):
        self.name = name
        self.level = level
        self.start = start
        self.course_map = {}

    def add_course(self, course):
        self.course_map[course.id] = course

    def get_course(self, id):
        return self.course_map[id]


# University 1---0..1 Student
class Student:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        

# Program owns the Course and Student * ---- * Course
class Course:
    def __init__(self, credit, id, lecturer, name, semester, student_list):
        self.credit = credit
        self.id = id
        self.lecturer = lecturer
        self.name = name
        self.semester = semester
        self.student_list = student_list

        

# Course * --Gives-- 1 Lecturer
class Lecturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getCourse(self, id):
        return self.course_map[id]

# Take class      Student * --Takes-- * Course
class Takes:
    def __init__(self, grade, scores, student, course):
        self.grade = grade
        self.scores = scores
        self.student = student
        self.course = course

# takes * ---- 1 Transcript
class Transcript:
    def __init__(self, id, student, takes_list):
        self.id = id
        self.student = student
        self.takes_list = takes_list

    def get_takes(self, id):
        return self.takes_list[id]

    def print_transcript(self):
        print("Transcript for " + self.student.name)
        for takes in self.takes_list:
            print(takes.course.name + " : " + takes.grade)




