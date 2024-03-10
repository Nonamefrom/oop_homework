class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course].append(grade)
            return f"Оценка успешно добавлена лектору {lecturer.name} {lecturer.surname} за курс {course}"
        else:
            return 'Ошибка: проверьте данные'

    @property
    def average_homework_grade(self):
        avg_homework_grades = {course: sum(grades) / len(grades) if grades else 0 for course, grades in
                               self.grades.items()}
        avg_homework_grade = sum(avg_homework_grades.values()) / len(avg_homework_grades) if avg_homework_grades else 0
        return avg_homework_grade

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за домашние задания: {self.average_homework_grade:.1f}"
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other):
        if self.average_homework_grade == other.average_homework_grade:
            return f"{self.name} имеет среднюю оценку за домашние задания, равную {other.name}"
        else:
            return f"{self.name} и {other.name} имеют разные средние оценки за домашние задания"

    def __ne__(self, other): # необходим, т.к. вызов != не обратен ==(__eq__) а вызывает 'not a == b'
        if self.average_homework_grade != other.average_homework_grade:
            return f"{self.name} и {other.name} имеют разную среднюю оценку за домашние задания"
        else:
            return f"{self.name} и {other.name} имеют одинаковую среднюю оценку за домашние задания"

    def __lt__(self, other):
        if self.average_homework_grade < other.average_homework_grade:
            return f"{self.name} имеет оценку ниже за домашние задания, чем {other.name}"
        else:
            return f"{self.name} имеет оценку выше за домашние задания, чем {other.name}"

    def __le__(self, other):
        if self.average_homework_grade <= other.average_homework_grade:
            return f"{self.name} имеет оценку ДЗ ниже или равную оценке {other.name}"
        else:
            return f"{self.name} имеет оценку ДЗ выше или равную оценке {other.name}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    @property
    def average_lecture_grade(self):
        avg_lecture_grades = {course: sum(grades) / len(grades) if grades else 0 for course, grades in
                                self.grades.items()}
        avg_lecture_grade = sum(avg_lecture_grades.values()) / len(avg_lecture_grades) if avg_lecture_grades else 0
        return avg_lecture_grade

    def __str__(self):
        sum_grades = sum(sum(grades) / len(grades) for grades in self.grades.values())
        avg_lecture_grade = sum_grades / len(self.grades) if self.grades else 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_lecture_grade:.1f}"

    def __eq__(self, other):
        if self.average_lecture_grade == other.average_lecture_grade:
            return f"{self.name} имеет среднюю оценку за лекции, равную {other.name}"
        else:
            return f"{self.name} и {other.name} имеют разные средние оценки за лекции"

    def __ne__(self, other): # необходим, т.к. вызов != не обратен ==(__eq__) а вызывает 'not a == b'
        if self.average_lecture_grade != other.average_lecture_grade:
            return f"{self.name} и {other.name} имеют разную среднюю оценку за домашние задания"
        else:
            return f"{self.name} и {other.name} имеют одинаковую среднюю оценку за домашние задания"

    def __lt__(self, other):
        if self.average_lecture_grade < other.average_lecture_grade:
            return f"{self.name} имеет оценку ниже за лекции, чем {other.name}"
        else:
            return f"{self.name} имеет оценку выше за лекции, чем {other.name}"

    def __le__(self, other):
        if self.average_lecture_grade <= other.average_lecture_grade:
            return f"{self.name} имеет оценку за лекции ниже или равную оценке {other.name}"
        else:
            return f"{self.name} имеет оценку за лекции выше или равную оценке {other.name}"


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course not in student.grades:
                student.grades[course] = []
            student.grades[course].append(grade)
            return f"Оценка успешно добавлена студенту {student.name} {student.surname} за курс {course}"
        else:
            return 'Ошибка'


def average_homework_grade(students, course):
    grades = [grade for student in students for grade in student.grades.get(course, [])]
    return f"Средняя оценка за ДЗ: {sum(grades) / len(grades) if grades else 0}"

def average_lecture_grade(lecturers, course):
    grades = [grade for lecturer in lecturers for grade in lecturer.grades.get(course, [])]
    return f"Средняя оценка лектора: {round(sum(grades) / len(grades) if grades else 0, 1)}"


# Создание экземпляров
student1 = Student("Ruoy", "Eman", "male")
student2 = Student("John", "Doe", "male")
lecturer1 = Lecturer("Some", "Buddy")
lecturer2 = Lecturer("Another", "Guy")
reviewer1 = Reviewer("Rev", "Buddy")
reviewer2 = Reviewer("Another", "Rev")

# Присвоение курсов
student1.courses_in_progress.append("Python")
student1.finished_courses.append("ООП")
student1.courses_in_progress.append("Git")
student2.courses_in_progress.append("Git")
student2.finished_courses.append("ООП")
lecturer1.courses_attached.append("Python")
lecturer2.courses_attached.append("Git")

# Выставление оценок
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Git", 10)
student2.rate_lecturer(lecturer2, "Git", 8)
student2.rate_lecturer(lecturer2, "Git", 6)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Python", 6)
reviewer2.rate_hw(student2, "Git", 9)
reviewer2.rate_hw(student1, "Git", 2)
reviewer2.rate_hw(student2, "Git", 1)

# Подсчет средних оценок

print(average_homework_grade([student1, student2], "Python"))
print(average_lecture_grade([lecturer1, lecturer2], "Python"))

# Вывод информации о классах
print(student1)
print(student2)
print(lecturer1)
print(reviewer1)
print(student1 == student2) # Сравниваем студентов по средней оценке за домашние задания
print(student1 != student2)
print(student1 > student2)
print(student1 >= student2)
print(student1 < student2)
print(student1 <= student2)
print(lecturer1 == lecturer2) # Сравниваем лекторов по средней оценке за лекции
print(lecturer1 != lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 >= lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 <= lecturer2)
