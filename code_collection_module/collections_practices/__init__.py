
class InitalCollectionPractices():

    def __init__(self,value:int=0) -> None:
        self.counter = value

    def changeCount(self,value) -> None:
        self.counter = value

    def getCounter(self) -> int:
        return self.counter
    
    def myDebugFunction(self) -> None:
        print(self.__module__)