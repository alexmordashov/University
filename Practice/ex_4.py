class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'Linal': [5], 'C++': [10]}
        self.average_grades = self.grades.values()

    def add_courses(self, course_name):
        if not course_name in self.finished_courses:
            self.finished_courses.append(course_name)
            if course_name in self.courses_in_progress:
                self.courses_in_progress.pop(course_name)
        else:
            print(f'Студент {self.name + self.surname} уже закончил курс {course_name}')

    def add_courses_in_progress(self, course_name):
        if not course_name in self.courses_in_progress:
            self.courses_in_progress.append(course_name)
        else:
            print(f'Студент {self.name + self.surname} уже закончил курс {course_name}')

    def rate_lecturer(self, lecturer, course, grade):
        if course in lecturer.courses_attached:
            if isinstance(grade, int) and grade >= 1 and grade <= 10:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course].append(grade)
                else:
                    lecturer.lecturer_grades[course] = grade
            else:
                return ('Оценка должна быть целым числом от 1 до 10')

    def get_average_grades(self, student):
        grades = self.grades
        return (sum(grades.values())) / len(grades)

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.average_grades} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress} \n" \
               f"Завершенные курсы: {self.finished_courses}"

    def __int__(self):
        return f"Кол-во курсов завершённых и в прогрессе: {len(self.courses_in_progress) + len(self.finished_courses)}"

    def __bool__(self):
        pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __int__(self):
        return f"Кол-во прилагаемых предметов: {len(self.courses_attached)}"

    def add_attached_courses(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Mentor.__init__(self, self.name, self.surname)
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: "


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(grade, int) and grade >= 1 and grade <= 10:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print('Оценка должна быть целым числом от 1 до 10')

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} "


Loshped = Student('Seryoga', 'Oreshkin', 'Male')
Angry = Reviewer('Jack', 'Fresko')
Bobbinson = Lecturer('Oleg', 'Tinkoff')
Angry.rate_student(Loshped, 'Linal', 5)
Angry.add_attached_courses('Linal')
Bobbinson.add_attached_courses('Linal')
Loshped.rate_lecturer(Bobbinson, 'Linal', 1)
print(Bobbinson.lecturer_grades)
print(str(Loshped))
print(Loshped.grades)
