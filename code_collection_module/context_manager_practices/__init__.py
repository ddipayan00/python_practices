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

# Python program showing
# file management using 
# context manager

class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()


def fileExample():
    # loading a file 
    try:
        print("File example")
        with FileManager('test.txt', 'w') as f:
            f.write('Test')
            print(1/0)

        # print(f.closed) 
    except Exception as e:
        print(f.closed)
        print(e)
         
def MongoExample(): 
    # Python program shows the
    # connection management 
    # for MongoDB
    from pymongo import MongoClient

    class MongoDBConnectionManager():
        def __init__(self, hostname, port):
            self.hostname = hostname
            self.port = port
            self.connection = None

        def __enter__(self):
            self.connection = MongoClient(self.hostname, self.port)
            return self.connection

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.connection.close()

    # connecting with a localhost
    with MongoDBConnectionManager('localhost', '27017') as mongo:
        collection = mongo.connection.SampleDb.test
        data = collection.find({'_id': 1})
        print(data.get('name'))
 
