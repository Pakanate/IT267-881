#สร้างพนักงานแผน IT
from empit import EmpIT

mike = EmpIT('001','Mike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#สร้างพนักงานแผน MKT
from empmkt import EmpMKT
anna = EmpMKT('002','Anna',35000)
anna.emp_detail()
anna.mkt_salary()

#Jess 003 เงินเดือน 45000 ทำงานอยู่ที่ Chiang Mai ได้คอมมิชชัน 35%
jess = EmpMKT('003','Jess',45000)
jess.add_location('Chiang Mai')
jess.add_commission(35)
jess.emp_detail()
jess.mkt_salary()