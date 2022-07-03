class Vehicle:
    def __init__(self,name,wheels,max,vin) -> None:
        self.name = name
        self.wheels = wheels
        self._maxspeed = max
        self.__vin = vin
    
    def set_vin(self,vin):
        self.__vin = vin
    
    def v_detail(self):
        print("==============")
        print(f'name: {self.name}')
        print("==============")
        print(f'wheels: {self.wheels}')
        print(f'max speed: {self._maxspeed}')
        print(f'vin: {self.__vin}')
