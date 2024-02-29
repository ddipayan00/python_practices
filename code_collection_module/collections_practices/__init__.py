def myDebugFunction():
    print(__file__)
    print(__name__)

class inital_collection_practices():
    def __init__(self,val:int=0) -> None:
        self.counter = val
    def changeCount(self,value):
        self.counter = value
    def getCounter(self):
        return self.counter
