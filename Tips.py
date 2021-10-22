#Statement trick
print("Calculates the average of two numbers")
print("The numbers are 4 & 8")
print("The average is ", (4+8)/2)
#Variable
'ถ้าเป็นตัวเลขใส่ได้เลย ถ้าเป็นตัวอักษรต้องมี""ครอบด้วย'
age=str(17)#, age="17"
print("I am"+ age + "years old")
age=17
print("I am", age, "years old")#suggest!!
#Data type 
# String
str = "string"
'0คือนับจากหัวไปท้าย'
'-1คือนับจากท้ายไปหัว'
print(type(str))
print(str)
print(str[0])
print(str[1])
print(str[2])
print(str[-3])
print(str[-2])
print(str[-1])
'ใช้lenเพื่อบอกจำนวนตัว'
print(len(str))
print(len(str)-2)
'เริ่มนับจาก0ไม่ใช่1' 
'นับจนถึงตัวก่อนตัวสุดท้าย(ไม่นับตัวlimit)'
'ใช้[]ครอบparameter ไม่ใช่()'
print(str[1:5])#= [-5:-1]
print(str[0:5])#= [:5]
print(str[-6:])#= [:]
#Number
'round(เลขทศนิยม,จำนวนตำแหน่งทศนิยมที่ต้องการ)'
f=1.60931
print(f)
print(round(1.60931,2))#, print(round(float,2)) ก็ได้
import math #เป็นการเรียกใช้functionของmoduleที่มีอยู่หรือสร้างขึ้นเองก็ได้
print(math.factorial(5))#1x2x3x4x5
print(math.ceil(2.2))#ปัดขึ้น
print(math.floor(2.8))#ปัดลง
#Tuple & List
'ใช้lenเพื่อบอกจำนวนของที่อยู่ในtuple'
'Tuple'#ไม่สามารถดัดแปลงแก้ไข โยกย้ายส่ายสะโพกได้ ("", "", "")
months=("January", "February", "March")
print(months)
print(type(months))
print(len(months))
print(months[-3:2])
'ใช้lenเพื่อบอกจำนวนของที่อยู่ในlist'
'List'#สามารถดัดแปลงแก้ไข โยกย้ายส่ายสะโพกได้ ["", "", ""]
fruit="grape, apple, banana"
fruit=["grape", "apple", "banana"]
print(fruit)
print(type(fruit))
print(len(fruit))
print(fruit[:2])
fruit[0]="orange"
print(fruit)
fruit.append("melon")#เพิ่มโดยการไปต่อท้าย
print(fruit)
fruit.insert(1,"cherry")#แทรกเข้าไปโดยต้องระบุ(ตำแหน่ง,"ตัวที่จะแทรก")
print(fruit)
fruit.pop()#ถ้าไม่ระบุ ค่าdefaultจะเอาตัวท้ายออกก่อน
print(fruit)
fruit.pop(2)#เอาตัวที่3ออก
print(fruit)
fruit.remove("banana")#เป็นการเอาออกแบบspecific
print(fruit)
fruit2=["grape", "apple"]
print(fruit2)
print(fruit+fruit2)#mergingสามารถทำได้ทั้งList+List, Tuple+Tuple, แต่!!! List+Tuple ไม่ได้
#dictionary
'ใช้ปีกกา{"" : "", "" : "", "" : ""}'
'เวลาเติมใช้[""] = "" '
person={"first_name" : "Pratsakorn", "last_name" : "Kittichadapong", "country_birth" : "Thailand"}
print(person)
print(type(person))
person["study"] = "Debsirin"
print(person)
person["hobby"] = ["coding", "listen to the music"]
print(person)
person["hobby"].append("play game")
print(person)
Key="hobby"
print(person[Key])
print(person.clear())
#While loop
person = []
while len(person) < 5:
    user=input("Type user name : ")
    person.append(user)
print(person)
#Try & Except
number = input("Type number : ")
try: 
    number = float(number)
    print("Number is  : ", number)
except:
    print("Invalid Number")
#Function
def Cm2m(cm):
    m=round(cm/100,2)
    return m
print(Cm2m(1000))