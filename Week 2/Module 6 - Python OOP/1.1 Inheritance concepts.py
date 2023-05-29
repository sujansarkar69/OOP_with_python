"""
1. Simple inheritance: parent class --> child class ex. (Gadget --> phone)

2. Multi-level inheritance: Grandpa ---> parent --> child

3. Multiple inheritance: Studnet(family, school, club)



"""

# Base class or parent class
# 1. Simple inheritance: parent class --> child class ex. (Gadget --> phone)
class BaseClass:
    def __init__(self) -> None:
        pass # Common attributes

# Derived class or child class
class DerivedClass(BaseClass):
    def __init__(self) -> None:
        super().__init__()


# 2. Multi-level inheritance: Grandpa ---> parent --> child
class BaseClass:
    def __init__(self) -> None:
        pass # Common attributes

class DerivedClass(BaseClass):
    def __init__(self) -> None:
        super().__init__()

class Derived_DerivedClass(DerivedClass):
    def __init__(self) -> None:
        super().__init__()


# 3. Multiple inheritance: Studnet(family, school, club)

class family:
    def __init__(self) -> None:
        pass

class school:
    def __init__(self) -> None: 
        pass

class derived_class(family, school):
    def __init__(self) -> None:
        family.__init__()
        school.__init__()