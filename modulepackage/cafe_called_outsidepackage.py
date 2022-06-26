#วิธีที่ 1
#from cafe.cafe_module import Desserts
#from cafe.cafe_module import Drinks
#desserts = Drinks()

#วิธีที่ 2
from cafe import cafe_module

desserts = cafe_module.Drinks()
print(desserts.show_desserts())

drinks = cafe_module.Drinks()
print(drinks.show_drinks())
drinks.add_drink('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())