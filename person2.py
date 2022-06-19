class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')

    

if __name__ =="__main__":
    #person1
    jessa = Person('Jessa','Female','Software Engineer',10)
    jessa.work()
    jessa.show()

    #person2
    jon = Person('Jon','Male','Doctor',15)
    jon.work()
    jon.show()

    #person
    lisa = Person('Lisa','Female','Singer',10)
    lisa.work()
    lisa.show()