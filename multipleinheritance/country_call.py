#country_call.py
from country import Country

#สร้าง object ของ country
c1 = Country('Thailand',513120,66.93)
c1.setcordinate(15.8700,100.9925)
c1.setcelsius(31)
c1.show_detail()

#สร้าง object ของประเทศ Norway
c2 = Country('Norway',385207,5.379)
c2.setcordinate(60.4720,8.4689)
c2.setcelsius(15)
c2.show_detail()