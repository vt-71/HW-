class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}  
        self.finished_courses = []   
        
    def add_courses(self, course_name):   
    # добавляет студенту пройденный курс 
        self.finished_courses.append(course_name)   
        
    def rate_lect(self, lecturer, course, grade):
    # Внесение оценки лекторам студентами
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
                return 'Ошибка'
            
    
            
    def _average_grade (self, grades):
    #  Средняя оценка
        counter = 0
        total_grades = 0
        for grades in grades.values():
            for grade in grades:               
                total_grades = total_grades + grade
                counter += 1
                if counter == 0:
                 return 0
        else:        
            return total_grades / counter
        
    def __lt__(self,other):
        # Сравнение средних оценок студентов 
            if isinstance(self, Student) and isinstance(other, Student):  
                if self._average_grade(self.grades) > other._average_grade(other.grades):
                    return (f'У {self.name} средняя оценка за ДЗ выше, чем у {other.name}')
                elif self._average_grade(self.grades) < other._average_grade(other.grades):
                    return(f'У {self.name} средняя оценка за ДЗ ниже, чем у {other.name}')
            else:
             print("Ошибка введенных данных!")        
             
    def __str__(self):
         res = f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за ДЗ: {self._average_grade(self.grades)}\n'\
               f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
         return res
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
           
        

        
class Lecturer(Mentor):
        def __init__(self, name, surname):
            super().__init__(name, surname)
            self.grades = {}   
        
        def _average_grade (self, grades):
            return Student._average_grade (self, grades)
                    
   
        def __str__(self):
         res = f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {Student._average_grade(self, self.grades)}\n'
         return res  
     

        def __lt__(self,other):
        # Сравнение средних оценок Лекторов 
            if isinstance(self, Lecturer) and isinstance(other, Lecturer):  
                if Student._average_grade(self, self.grades) > Student._average_grade(self, other.grades):
                    return (f'У {self.name} средняя оценка за лекции выше, чем у {other.name}')
                elif self._average_grade(self.grades) < other._average_grade(other.grades):
                    return(f'У {self.name} средняя оценка за лекции ниже, чем у {other.name}')
            else:
                print("Ошибка введенных данных!")         

class Reviewer(Mentor):
        def __init__(self, name, surname):
            super().__init__(name, surname)

             
        def rate_hw(self, student, course, grade):  
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] = student.grades[course] + [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
            
        def __str__(self):
         res = f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'
         return res  

student_1 = Student('Ruoy', 'Eman', 'men')
student_2 = Student('Natalia', 'Shirokova', 'woman')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python', 'GIT']
student_1.add_courses('Введение в Python')
student_2.add_courses('ООП')



Reviewer_1 = Reviewer('Li', 'Pack')
Reviewer_1.courses_attached += ['Python']
Reviewer_2 = Reviewer('Gon', 'Ruby')
Reviewer_2.courses_attached += ['Python', 'GIT']


Lecturer_1 = Lecturer('Vadimir', 'Petrov')
Lecturer_1.courses_attached += ['Python']
Lecturer_2 = Lecturer('Sergey', 'Ponomarev')
Lecturer_2.courses_attached += ['Python', 'GIT']

 
Reviewer_1.rate_hw(student_1, 'Python', 20)
Reviewer_1.rate_hw(student_1, 'Python', 8)
Reviewer_2.rate_hw(student_2, 'GIT', 8)


student_1.rate_lect(Lecturer_2, 'Python', 9)
student_1.rate_lect(Lecturer_2, 'Python', 7)
student_2.rate_lect(Lecturer_1, 'GIT', 3)

Lecturer_1._average_grade(Lecturer_1.grades)
Lecturer_2._average_grade(Lecturer_2.grades)

print(student_1)
print(Lecturer_2)
print(Reviewer_1)

print(student_1 < student_2)
print(Lecturer_2 > Lecturer_1)
# print(student_1.__dict__)
# print(Lecturer_1.__dict__)
# print(Reviewer_1.__dict__)


