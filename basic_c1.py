from pythondatalearning.basic_c2 import tax_calculate

name="username"
age = 35
place="chennai"
remote = False

print(type(age))

report_list = [7,8,10,0,6]
user_map = {"name":"userxxx", "age":30}  #map or dict
user_1 = {"basic": 12222, "HRA": 5555, "LTA": 60000}

basic =98000
hra = 6700

fixedpay   = basic +hra
variablpay = basic + hra + 100

print(fixedpay)
print(variablpay)




#condition
if age < 31:
    insurance = 2000
elif age> 31 :
    insurance = 4500

print(insurance)

birthdaylist = ["AShok", "AShwin","AADhi", "Haripriya"]

for i in  birthdaylist :
    print("happy Bday "+ i)

tax_calculate("add",4,6)

if __name__ == '__main__':
    print("complete")