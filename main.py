# Добавлен класс Студенты
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    # Метод позволяет добавлять оконченные курсы

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # метод позволяет выставлять оценки лекторам за лекции (задание №2)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                 lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # метод позволяет просчитать среднюю оценку за домашние задания (задание №3)

    def stat(self):
            avg_grades = 0
            sum_grade = 0
            for key in self.grades:
                for elem in self.grades[key]:
                    sum_grade = sum_grade + elem
                if sum_grade != 0:
                    avg_grades = sum_grade / (len(self.grades[key]))
            return avg_grades
    # метод позволяет выводить на экран в удобном виде для пользователя информацию

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.stat()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
# Метода сравнения лекторов по средней оценке за лекции:

    def __lt__(self, other):
        return self.stat() < other.stat()
    def __eq__(self, other):
        return self.stat() == other.stat()
    def __le__(self, other):
        return self.stat() == other.stat()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def stat(self):
            avg_grades = 0
            sum_grade = 0
            for key in self.grades:
                for elem in self.grades[key]:
                    sum_grade = sum_grade + elem
                if sum_grade != 0:
                    avg_grades = sum_grade / (len(self.grades[key]))
            return avg_grades

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.stat()}"

    def __lt__(self, other):
        return self.stat() < other.stat()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
#
cool_mentor = Reviewer('Rew', 'Surname')
cool_mentor.courses_attached += ['Python']
#
# best_lecturer = Lecturer('Tonny', 'Stark')
# best_lecturer.courses_attached += ['Python']
#
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
#
# best_student.rate_lect(best_lecturer, 'Python', 10)
# best_student.rate_lect(best_lecturer, 'Python', 9)
# best_student.rate_lect(best_lecturer, 'Python', 10)

some_reviewer = Reviewer('Some', 'Body')
print(some_reviewer)
# print("Имя: "+(some_reviewer.name))
# print("Фамилия: "+(some_reviewer.surname))
#
# print(best_student.grades)
# print(best_lecturer.grades)
some_lecturer = Lecturer('LecturerName', 'LecturerSn')
some_student = Student('StName', 'StSn', 'gen')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']
some_lecturer.courses_attached += ['Python']
cool_mentor.rate_hw(some_student, 'Python', 10)
cool_mentor.rate_hw(some_student, 'Python', 10)
cool_mentor.rate_hw(some_student, 'Python', 7)
some_student.rate_lect(some_lecturer, 'Python', 10)
some_student.rate_lect(some_lecturer, 'Python', 9)
some_student.rate_lect(some_lecturer, 'Python', 10)

print(some_lecturer)
print(some_student)
print(best_student)
print("сравнение"+str(best_student.__lt__(some_student)))
print("сравнение1"+str(best_student.__eq__(some_student)))
print("сравнени2"+str(best_student.__le__(some_student)))
# Экземпляры класса Студент
some_student_1 = Student('Игорь', 'Белоконь', 'ПолСтудента')
some_student_1.courses_in_progress += ['Python']
cool_mentor.rate_hw(some_student_1, 'Python', 10)
cool_mentor.rate_hw(some_student_1, 'Python', 7)
cool_mentor.rate_hw(some_student_1, 'Python', 9)
some_student_2 = Student('Ирина', 'Ирмина', 'ПолСтудента')
some_student_2.courses_in_progress += ['Python']
cool_mentor.rate_hw(some_student_2, 'Python', 10)
cool_mentor.rate_hw(some_student_2, 'Python', 7)
cool_mentor.rate_hw(some_student_2, 'Python', 10)

#Экземпляры класса Лектор
some_lecturer_1 = Lecturer('Dart', 'Vaider')
some_lecturer_2 = Lecturer('Magistre', 'Yoda')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Python']
some_student_1.rate_lect(some_lecturer_1, 'Python', 10)
some_student_1.rate_lect(some_lecturer_2, 'Python', 10)
some_student_1.rate_lect(some_lecturer_1, 'Python', 9)
some_student_1.rate_lect(some_lecturer_2, 'Python', 10)
some_student_1.rate_lect(some_lecturer_2, 'Python', 9)

obj_list = [some_student_1, some_student_2]
lect_list = [some_lecturer_1, some_lecturer_2]

for elem in obj_list:
    avg_grades = 0
    sum_grade = 0
    for elem in obj_list:
        sum_grade = sum_grade + elem.stat()
    if sum_grade != 0:
        avg_grades = sum_grade / (len(obj_list))
print("средняя оценка по всем студентам "+str(avg_grades))

for elem_1 in lect_list:
    avg_grades = 0
    sum_grade = 0
    for elem_1 in lect_list:
        sum_grade = sum_grade + elem_1.stat()
    if sum_grade != 0:
        avg_grades = sum_grade / (len(lect_list))
print("средняя оценка по всем лекторам "+str(avg_grades))

# вызовем методы для some_lecturer_1 и some_lecturer_2

print(some_lecturer_1)
print(some_lecturer_2)
print("сравнение "+str(some_lecturer_1.__lt__(some_lecturer_2)))

# вызовем методы для some_student_1 и some_student_2

print(some_student_1)
print(some_student_2)
print("сравнение "+str(some_student_1.__lt__(some_student_2)))