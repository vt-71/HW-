class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}
        
        
    def rate_lect(self, lecturer, course, grade):
    # Внесение оценки лекторам студентами
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
                return 'Ошибка'
            
    def averade_grade (self, grades):
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
        
    def __str__(self) -> str:
         res = f'Средняя оценка за ДЗ = {self.averade_grade ()}'
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
            
        def averade_grade (self, grades):
            print(Student.averade_grade (self, grades))

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

student_1 = Student('Ruoy', 'Eman', 'men')
student_2 = Student('Natalia', 'Shirokova', 'woman')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python', 'GIT']


Reviewer_1 = Reviewer('Li', 'Pack')
Reviewer_1.courses_attached += ['Python']
Reviewer_2 = Reviewer('Gon', 'Ruby')
Reviewer_2.courses_attached += ['Python', 'GIT']


Lecturer_1 = Lecturer('Vadimir', 'Petrov')
Lecturer_1.courses_attached += ['Python']
Lecturer_2 = Lecturer('Sergey', 'Ponomarev')
Lecturer_2.courses_attached += ['Python', 'GIT']
 
Reviewer_1.rate_hw(student_1, 'Python', 10)
Reviewer_1.rate_hw(student_1, 'Python', 8)
Reviewer_2.rate_hw(student_2, 'GIT', 6)
# print(student_1.__dict__)
# print(student_1.__dict__)
print(student_2.averade_grade(student_1.grades))
print(student_1.averade_grade(student_2.grades))
# print(student_2)

student_1.rate_lect(Lecturer_2, 'Python', 9)
student_1.rate_lect(Lecturer_2, 'Python', 7)
student_2.rate_lect(Lecturer_1, 'GIT', 3)
# print(Lecturer_2.grades)
# print(Lecturer_1.averade_grade(Lecturer_1.grades))
# print(student_1.averade_grade(Lecturer_1.grades))

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
