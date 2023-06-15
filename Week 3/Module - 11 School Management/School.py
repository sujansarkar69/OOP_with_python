class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named {className}')

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        if 70 <= marks < 80:
            return 'A'
        if 60 <= marks < 70:
            return 'A-'
        if 50 <= marks < 60:
            return 'B'
        if 40 <= marks < 50:
            return 'C'
        if 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.50,
            'D': 2.00,
            'F': 0.00,
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 4.0 <= value < 4.5:
            return 'A'
        elif 4.5 <= value < 4.5:
            return 'A-'
        elif 3.0 <= value < 3.5:
            return 'B'
        elif 2.5 <= value < 3.0:
            return 'C'
        elif 2.0 <= value < 2.5:
            return 'D'
        else:
            return 'F'
    

    def __repr__(self) -> str:
        print('--------ALL CLASSROOM--------')
        for key, value in self.classrooms.items():
            print(key)

        print('-----------STUDENTS----------')
        eight = self.classrooms['eight']
        print('Total Students: ', len(eight.students))
        for student in eight.students:
            print('Name: ',student.name)
        
        print('-----------SUBJECTS----------')
        for sub in eight.subjects:
            print(f'Subject: {sub.name}, Teacher: {sub.teacher.name}')

        print('-----STUDENTS EXAM MARKS-----')
        for student in eight.students:
            for key, value in student.marks.items():
                print(f'Name: {student.name}, Subject: {key} -> marks: {value}, Grade: {student.subject_grade[key]}')
            print('--->')

        print('----STUDENTS FINAL GRADE----')
        for student in eight.students:
            print(f'Name: {student.name}, Final Grade: {student.grade}')
        
        return ''

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name} - {len(self.students) + 1}'
        student.id = serial_id  
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        # take exam
        for sub in self.subjects:
            sub.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'
    
    def get_top_student(self):
        pass

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.max_marks = 100
        self.pass_marks = 33
        self.teacher = teacher

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
    
       