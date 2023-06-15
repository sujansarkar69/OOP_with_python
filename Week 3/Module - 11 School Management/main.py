from School import School, ClassRoom, Subject
from Person import Student, Teacher
def main():
    school = School('CPI', 'Cumilla')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students:
    sujan = Student('Sujan', eight)
    school.student_admission(sujan)
    seyam = Student('Seyam', eight)
    school.student_admission(seyam)
    rakib = Student('Rakib', eight)
    school.student_admission(rakib)

    # subject
    physics_teacher = Teacher('Amin')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Niloy')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Ayesha')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()
    print(school)

if __name__ == '__main__':
    main()