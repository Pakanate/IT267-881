#countrysubclass.py
from countryabstract import Country

class Europe(Country):
    def __init__(self, name, population) -> None:
        super().__init__(name, population)
        self.__location = ""
        self.__capital = 0
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self,location):
        self.__location = location
    
    @property
    def capital(self):
        return self.__capital
    @capital.setter
    def capital(self,capital):
        self.__capital = capital
    
    def show_detail(self):
        print("==== Europe ====")
        print(f"country: {self.name}")
        print(f"capital: {self.capital}")
        print(f"population: {self.population:,}")
        print(f"location: {self.location}")
        
class Asia(Country):
    def __init__(self, name, population) -> None:
        super().__init__(name, population)
        self.__gdp = 0
    
    @property
    def gdp(self):
        return self.__gdp
    @gdp.setter
    def gdp(self,gdp):
        self.__gdp = gdp
    
    def show_detail(self):
        print("==== Asia ====")
        print(f"country: {self.name}")
        print(f"population: {self.population:,}")
        print(f"gdp: {self.gdp}")