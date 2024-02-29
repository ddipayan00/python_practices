from collections import Counter
from typing import Any
import  traceback2 as tb
class InitalCollectionPractices():

    def __init__(self,value:int=0) -> None:
        self.counter = value

    def changeCount(self,value) -> None:
        self.counter = value

    def getCounter(self) -> int:
        return self.counter
    
    def myDebugFunction(self) -> None:
        print(self.__module__)

class CollectionCounter():
    # (class) variable vs (instance | newly created object) variable 
    # https://stackoverflow.com/questions/65804341/creating-new-object-instance-but-old-instance-was-changed-in-python
    
    def __init__(self,value=None,keyWordArgValue=None) -> None:
        self.counter_obj = None 
        self.originalValue = value
        self.originalKeyWordArgValue = keyWordArgValue
        self.createCounter()
        print(f"{self.counter_obj=}")
        
    def getCounterObj(self) -> Counter:
        return self.counter_obj
    
    # sample code -----------------------------------------
    def copyCounterObj(self) -> Counter:
        return self.counter_obj.copy()
    
    def clearCounterObj(self) -> None:
        self.value = None
        self.keyWordArgValue = None
        return self.counter_obj.clear()
    
    def elementsOfCounterObj(self):
        return self.counter_obj.elements()
    
    def getCounterObjMethod(self,__key) -> (int | None):
        return self.counter_obj.get(__key)
    
    def mostCommonOfCounterObj(self,val) -> list[tuple[Any, int]]:
        return self.counter_obj.most_common(val)
    
    # Factory reset
    def resetToFactory(self):
        try:
            print("Trying to factory reset....")
            self.createCounter()
            print("Factory reset done!")
        except Exception as error:
            print("Error while factory reset!","Error : ",error,sep="\n")
        
    
    def testRunner(self):
        # sample testing code ---------------------------
        try:
            print("Test starting....")
            elementsOfCounterObjResponse = self.elementsOfCounterObj()
            getCounterObjMethodResponse = self.getCounterObjMethod("B")
            clearCounterObjResponse = self.clearCounterObj()
            copyCounterObjResponse = self.copyCounterObj()
            getCounterObjResponse = self.getCounterObj()
            mostCommonOfCounterObjResponse = self.mostCommonOfCounterObj(1)
            clearCounterObjResponse = self.clearCounterObj()
            print("elementsOfCounterObjResponse: ",
                elementsOfCounterObjResponse,
                "getCounterObjMethodResponse: ",
                getCounterObjMethodResponse,
                "clearCounterObjResponse: ",
                clearCounterObjResponse,
                "copyCounterObjResponse: ",
                copyCounterObjResponse,
                "getCounterObjResponse: ",
                getCounterObjResponse,
                "mostCommonOfCounterObjResponse: ",
                mostCommonOfCounterObjResponse,
                "clearCounterObjResponse : ",
                clearCounterObjResponse,
                sep="\n"
            )
            assert isinstance(copyCounterObjResponse,Counter) != False 
            assert bool(elementsOfCounterObjResponse) != False
            assert isinstance(getCounterObjResponse,Counter) != False
            assert isinstance(1,int) == isinstance(getCounterObjMethodResponse,int) or getCounterObjMethodResponse == None
            assert mostCommonOfCounterObjResponse != None
            assert clearCounterObjResponse == None
            print("Test done!")
            self.resetToFactory()
            print(f"{self.counter_obj=}")
        except AssertionError as error:
            tb.print_exc()
            print("error : ",error)

    def createCounter(self):
        value = self.originalValue
        keyWordArgValue = self.originalKeyWordArgValue
        if value and keyWordArgValue:
                raise Exception("Pass only one -> value or keyWordArgValue")
        import sys
        if self.counter_obj != None:
            print(sys.getsizeof(self.counter_obj))
            self.counter_obj = None
            print(sys.getsizeof(self.counter_obj))

        if value:
            self.counter_obj = Counter(value)
        else:
            if keyWordArgValue:
                self.counter_obj = Counter(**keyWordArgValue)
            else:
                self.counter_obj = Counter()
        print(sys.getsizeof(self.counter_obj))

    # TODO UpadteCounter (value | keyWordArgValue)



    
