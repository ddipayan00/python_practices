import traceback2 as tb
from code_collection_module import (
    context_manager_practices as ctp,
    collections_practices as collp
)

if __name__ == "__main__":
    try:
        value = ['B','B','A','B','C','A','B','B','A','C'] if True else False
        keyWordArgValue = {'A':2,'3':1} if not True else False
        print(value,keyWordArgValue)
        counterObj = collp.CollectionCounter(value=value,keyWordArgValue=keyWordArgValue)
        counterObj.testRunner()
        temp = counterObj.getCounterObj()
        temp = counterObj.mostCommonOfCounterObj(1)
        print(f"{temp=}")
    except:
        tb.print_exc()