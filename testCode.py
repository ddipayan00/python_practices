from code_collection_module import (collections_practices)

if __name__ == "__main__":
    obj = collections_practices.inital_collection_practices(val=10)
    print(obj.getCounter())
    obj.changeCount(10)
    print(obj.getCounter())
    collections_practices.myDebugFunction()