class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.subject}'

class School:

    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
        
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return f'Not enough money.'
        else:
            id = len(self.students) + 1
            student = Student(name, 'python', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}tk.'

    def __repr__(self) -> str:
        print(f'Wellcome to {self.name}.')
        print('------OUR TEACHERS------')
        for teacher in self.teachers:
            print(teacher)
        print('------OUR STUDENTS------')
        for student in self.students:
            print(student)
        return 'All done for now.'


# sujan = Student('Sujan Sarkar', 14, 62)
# teacher = Teacher('XYZ', 'Algorithm', 101)
# print(sujan)
# print(teacher)

phitron = School('Phitron')
phitron.enroll('Sujan Sarkar',6500)
phitron.enroll('Rasel Choy',6500)
phitron.enroll('Rafiq',6500)
phitron.enroll('Mahfuz',6500)

phitron.add_teacher('Jhankar mahbub','Python')
phitron.add_teacher('Decap','DS')
phitron.add_teacher('xyz','zyx')

print(phitron)

