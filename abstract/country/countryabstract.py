#countryabstract.py
from abc import ABC, abstractclassmethod, abstractmethod

class Country(ABC):
    def __init__(self,name,population) -> None:
        super().__init__()
        self.name = name
        self.population = population
    
    @abstractmethod
    def show_detail(self):
        pass