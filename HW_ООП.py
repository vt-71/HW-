class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}
        
        
    def rate_rw(self, reviewer, course, grade):
        if isinstance(reviewer, Reviewer) and course in reviewer.courses_attached:
                if course in reviewer.grades:
                    reviewer.grades[course] += [grade]
                else:
                    reviewer.grades[course] = [grade]
        else:
                return 'Ошибка'
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

        
class Lecturer(Mentor):
        def __init__(self, name, surname):
            super().__init__(name, surname)

class Reviewer(Mentor):
        def __init__(self, name, surname):
            super().__init__(name, surname)
            self.grades = {}
             
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
Lecturer_2 = Lecturer('Sergey', 'Ponomarev')
# Lecturer.courses_attached += ['Python']
 
Reviewer_1.rate_hw(student_1, 'Python', 10)
Reviewer_1.rate_hw(student_1, 'Python', 8)
Reviewer_2.rate_hw(student_2, 'GIT', 6)


student_1.rate_rw(Reviewer_2, 'Python', 9)
student_1.rate_rw(Reviewer_1, 'Python', 7)
student_2.rate_rw(Reviewer_2, 'GIT', 5)
print(Reviewer_1.__dict__)
print(Reviewer_2.__dict__)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
