from collections import (
    Counter,
    OrderedDict,
    ChainMap,
    namedtuple,
    deque,
    UserDict,
    UserList,
    UserString
)

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

# Note first time warming up class methods class variable and all essential stuffs for python class based development 
# Next time I will be not create all method seperately as an example like CollectionCounter
# In near future if I need to learn something only then I will opt for methos and all.
# This time as an example in OrderedDictClass I will show or practice all the use cases of OrderDict as an example one or two method 
# Even I can create a simple method on the specfic collection to practice all the use cases
# I will do that probably when I am confident with the class based approach.     
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
class OrderedDictClass():
    pass 
class ChainMapClass():
    def __init__(self) -> None:
        pass

    def ChainMapMethod(self):
        #sample code
        d1 = {'a': 1, 'b': 2} 
        d2 = {'c': 3, 'd': 4} 
        d3 = {'e': 5, 'f': 6} 
        c = ChainMap(d1, d2, d3)  
        print(c)
        print(c['a']) 
        print(c.values()) 
        print(c.keys())
    
    def useCase(self):
        # suppose you have different api response you want to combine them into one and you have some work to do on that then you can use ChainMap
        # it's like using list extend() method for list joinning
        #  
        # fruits = ['apple', 'banana', 'cherry']
        # points = (1, [4,2], 5, 9)
        # fruits.extend(points)
        # print(fruits)

        # Merge dictionaries with .update() is diffrent from chaining


        for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
        vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
        print(f"{for_adoption=}")
        print(f"{vet_treatment=}")
        pets = ChainMap(for_adoption, vet_treatment)

        print(pets["turtles"])
        return None
class namedtupleClass():
    # Python code to demonstrate namedtuple() 
    def __init__(self) -> None:
        # Declaring namedtuple() 
        Student = namedtuple('Student',['name','age','DOB']) 
            
        # Adding values 
        S = Student('Nandini','19','2541997') 
            
        # Access using index 
        print ("The Student age using index is : ",end ="") 
        print (S[1]) 
            
        # Access using name 
        print ("The Student name using keyname is : ",end ="") 
        print (S.name)
class dequeClass():
    def __init__(self) -> None:
        # Python code to demonstrate deque 
        # Declaring deque 
        queue = deque(['name','age','DOB']) 
            
        print(queue)
        de = deque([1,2,3])  
        
        # using append() to insert element at right end   
        # inserts 4 at the end of deque  
        de.append(4)  
            
        # printing modified deque  
        print ("The deque after appending at right is : ")  
        print (de)  
            
        # using appendleft() to insert element at left end   
        # inserts 6 at the beginning of deque  
        de.appendleft(6)  
            
        # printing modified deque  
        print ("The deque after appending at left is : ")  
        print (de)
class UserDictClass():

    # This is a good example of using UserDict collection class
    def __init__(self) -> None:
        # Creating a Dictionary where 
        # deletion is not allowed 
        class MyDict(UserDict): 
                
            # Function to stop deletion 
            # from dictionary 
            def __del__(self): 
                raise RuntimeError("Deletion not allowed") 
                    
            # Function to stop pop from 
            # dictionary 
            def pop(self, s = None): 
                raise RuntimeError("Deletion not allowed") 
                    
            # Function to stop popitem 
            # from Dictionary 
            def popitem(self, s = None): 
                raise RuntimeError("Deletion not allowed") 
                
        # Driver's code 
        d = MyDict({'a':1, 
            'b': 2, 
            'c': 3}) 
            
        d.pop(1)
        print(d)
class UserListClass():
    def __init__(self) -> None:
        # Python program to demonstrate User list 
        # Creating a List where 
        # deletion is not allowed 
        class MyList(UserList): 
                
            # Function to stop deletion 
            # from List 
            def remove(self, s = None): 
                raise RuntimeError("Deletion not allowed") 
                    
            # Function to stop pop from 
            # List 
            def pop(self, s = None): 
                raise RuntimeError("Deletion not allowed") 
                
        # Driver's code 
        L = MyList([1, 2, 3, 4]) 
            
        print("Original List") 
            
        # Inserting to List" 
        L.append(5) 
        print("After Insertion") 
        print(L) 
            
        # Deleting From List 
        L.remove()
class UserStringClass():
    def __init__(self) -> None:
        # Python program to demonstrate 
        # userstring  
        # Creating a Mutable String 
        class Mystring(UserString): 
                
            # Function to append to 
            # string 
            def append(self, s): 
                self.data += s 
                    
            # Function to remove from 
            # string 
            def remove(self, s): 
                self.data = self.data.replace(s, "") 
                
        # Driver's code 
        s1 = Mystring("Geeks") 
        print("Original String:", s1.data) 
            
        # Appending to string 
        s1.append("s") 
        print("String After Appending:", s1.data) 
            
        # Removing from string 
        s1.remove("e") 
        print("String after Removing:", s1.data)

