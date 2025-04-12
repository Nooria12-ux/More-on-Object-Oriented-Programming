class IOString:
    
    #CONSTRUCTOR
    def __init__(self):
        self.str1 = ""
        
    #METHOD/FUNCTION
    def getString(self):
        self.str1 = input("Enter a string: ")
        
    #METHOD/FUNCTION
    def printString(self):
        print(f"Result is: {self.str1.upper()}")
        
object1 = IOString()

object1.getString()
object1.printString()
                