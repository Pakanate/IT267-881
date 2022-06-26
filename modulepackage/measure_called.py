from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    #รับค่าตัวเลขจาก user ได้
    number = float(input('Enter number: '))
    #ให้ user เลือกได้ว่าต้องการแปลงค่าเป็น inch หรือ cm
    choice = input('Choose menu to convert (1: inch, 2:cm): ')
    
    if choice == '1': 
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.inch_cm(number):.2f} cm')
    else:
        print('Choose wrong menu')


