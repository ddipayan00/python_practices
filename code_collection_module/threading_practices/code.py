from os import sep
def main():
    try:
        module_name = __file__.split(sep)[-2]
        file = __file__.split(sep)[-1]
        print("Module Name: ",module_name)
        print("File Name: ",file)
    except:
        pass

if __name__ == "__main__":
    main()