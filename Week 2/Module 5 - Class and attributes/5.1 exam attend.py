import random
class Exam:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def attend(self):
        print(f'{self.name} attend to the {self.subject} exam.')

    def get_marks(self):
        return random.randint(70,100)
    
candidate = Exam('Sujan', 'CS')
candidate.attend()
print(f'you got {candidate.get_marks()} marks in {candidate.subject} subject.')