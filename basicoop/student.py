class Student:
    def __init__(self,id:str,name:str,major="IT") -> None:
        self.id = id
        self.name =  name
        self.major = major

    def display_detail(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
    
    def __del__(self):
        print("Object was destroyed")

if __name__ =="__main__":
    jess = Student("111","Jessica","IT")
    jess.display_detail()

    john = Student("112","John","MKT")
    john.display_detail()

    james = Student("113","James")
    james.display_detail()
