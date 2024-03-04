import traceback2 as tb
from code_collection_module import (
    context_manager_practices as ctp,
    collections_practices as collp,
    decorators_practices as decorp
)

if __name__ == "__main__":
    print()


    # CollectionCounter --------------------------------------------------------------------------
    # try:
    #     value = ['B','B','A','B','C','A','B','B','A','C'] if True else False
    #     keyWordArgValue = {'A':2,'3':1} if not True else False
    #     print(value,keyWordArgValue)
    #     counterObj = collp.CollectionCounter(value=value,keyWordArgValue=keyWordArgValue)
    #     counterObj.testRunner()
    #     temp = counterObj.getCounterObj()
    #     temp = counterObj.mostCommonOfCounterObj(1)
    #     print(f"{temp=}")

    # except:
    #     tb.print_exc()


    # ChainMapClass --------------------------------------------------------------------------
    # try:
    #     ChainMapClass_obj = collp.ChainMapClass()
    #     # ChainMapClass_obj.ChainMapMethod()
    #     ChainMapClass_obj.useCase()
        
    # except:
    #     tb.print_exc()

    # namedtupleClass --------------------------------------------------------------------------
    # try:
    #     namedtupleClassObj = collp.namedtupleClass() 
    # except:
    #     tb.print_exc()


    # dequeClass --------------------------------------------------------------------------
    # try:
    #     collpDequeClass = collp.dequeClass()
    # except:
    #     tb.print_exc()

    # UserDictClass --------------------------------------------------------------------------

    # try:
    #     UserDictClassObj = collp.UserDictClass()
    # except:
    #     pass 

    # UserListClass --------------------------------------------------------------------------

    # try:
    #     UserListClassObj = collp.UserListClass()
    # except:
    #     pass

    # UserStringClass --------------------------------------------------------------------------

    # try:
    #     UserStringClassObj = collp.UserStringClass()
    # except:
    #     pass


    # Context Manager example --------------------------------------------------------------------------
    # try:
    #     ctp.fileExample()
    #     # ctp.MongoExample()
    # except:
    #     pass

    
    decorp.Runner()
    









    print()