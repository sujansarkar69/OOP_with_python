class Family:
    def __init__(self, address) -> None:
        self.address = address
    
class School:
    def __init__(self, id, grade) -> None:
        self.id = id
        self.grade = grade

class Club:
    def __init__(self, sports) -> None:
        self.sports = sports

class Student(Family, School, Club):
    def __init__(self, address, id, grade, sports) -> None:
        School.__init__(self, id, grade)
        Club.__init__(self, sports)
        Family.__init__(self, address)

