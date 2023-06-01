class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return 'car started'

class Driver:
    def __init__(self) -> None:
        pass

# composition provide 'has a' relation 
# inheritance provide 'is a' relation

class car:
    def __init__(self) -> None:
        self.engine = Engine() # car has an engine
        self.driver = Driver() # car has a driver

