#country.py
from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop
    
    def getpopulation_density(self):
        return self.population / self.area
    
    def show_detail(self):
        #ชื่อประเทศ
        print(f'Country: {self.name}')

        #สถานที่ตั้ง latitude และ longitude
        print(self.getcordinate())

        #แสดงขนาดพื้นที่, จำนวนประชากร และความหนาแน่นของประชากร
        print(f'Area: {self.area:,.2f}')
        print(f'Population: {self.population:,.2f} Million')
        print(f'Density: {self.getpopulation_density():,.2f}')

        #Time Zone, Climate, Temperature, Weather
        print(f'TimeZone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperature(C): {self.celsius:.2f}')
        print(f'Temperature(F): {self.getfahrenheit():.2f}')
        print(f'Weather: {self.getweather()}')
        print()


