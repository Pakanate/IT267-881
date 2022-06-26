class Person:
    def __init__(self,name:str,gender:str,profession:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours:int):
        self.study = hours

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')

#person1
jessa = Person('Jessa','Female','Software Engineer')
jessa.work()
jessa.show()

#person2
jon = Person('Jon','Male','Doctor')
jon.study = 15
jon.work()
jon.show()

#person
lisa = Person('Lisa','Female','Singer')
lisa.study = 10
lisa.work()
lisa.show()