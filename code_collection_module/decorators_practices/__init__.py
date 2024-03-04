


class decoratorTestRunner():
    # code for testing decorator chaining 
    def __init__(self) -> None:
        def decor1(func): 
            def inner(): 
                print("before decor1")
                x = func() 
                print("In decor1 : ",x)
                return x * x 
            return inner 

        def decor(func): 
            def inner(): 
                print("before decor")
                x = func() 
                print("In decor : ",x)
                return 2 * x 
            return inner 
        
        @decor1
        @decor
        def num(): 
            print("num")
            return 10

        @decor
        @decor1
        def num2():
            print("num2")
            return 10
        
        @decor1
        @decor1
        def num3():
            print("num3")
            return 10
        
        @decor
        @decor
        def num4():
            print("num4")
            return 10
        

        print("First Function : ")
        print(num()) 
        print("\nSecond Function : ")
        print(num2())
        print("\nThird Function : ")
        print(num3())
        print("\nForth Function : ")
        print(num4())

class Runner():
    def __init__(self) -> None:
        from functools import wraps
        def my_decorator(f):
            @wraps(f)
            def wrapper(*args, **kwds):
                print('Calling decorated function')
                return f(*args, **kwds)
            return wrapper

        @my_decorator
        def example():
            """Docstring"""
            print('Called example function')

        example()
        print(example.__name__)

        print(example.__doc__)
        gta:int = 10
        x = gta.__doc__
        print(x)

        

if __name__ == "__main__":
    # decoratorTestRunner()
    Runner()