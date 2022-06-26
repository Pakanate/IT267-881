#เรียกใช้ package เพื่อเข้าถึงคลาส Customer, Account
from bank.customer import Customer
from bank.account import Account

#สร้าง object ของ customer ที่ชื่อ Paul
#ข้อมูลลูกค้า Paul, Nontaburi,012-345-6789
paul = Customer()
paul.new_customer()

#สร้าง object ของ account เพื่อเปิดบัญชีใหม่ให้กับ Paul
#ข้อมูลการเปิดบัญชี Saving, 0123-4578, 500
paul_acc = Account()
paul_acc.open_account(paul.name,'Saving','0123-4578',500)

#แสดงข้อมูลของ customer Paul
print(paul.cus_info())

#แสดงข้อมูลเงินคงเหลือในบัญชีของ Paul
print(paul_acc.display_balance())