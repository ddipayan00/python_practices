class HelloContextManager:
    def __enter__(self):
        print("Entering the context")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context")
        print("exc_type : ",exc_type)
        print("exc_value : ", exc_value)
        print("exc_tb : ", exc_tb)


def testRunner():       
    with HelloContextManager() as hello:
        try:
            print(hello)
            print(hello)
            # print(1/0)
            raise Exception("Error!")
        except Exception as e:
            print("Exception : ",e)