#คำนวณเกรด                 
x=int(float(input("Input your GRADE\n")))
'''ifถ้า..
   elifถ้าไม่ก็..
   elseอย่างอื่น'''
if 100>=x>=80:#4
 print("ur grade is 4")
elif 79>=x>=75:#3.5
 print("ur grade is 3.5")
elif 74>=x>=70:#3
 print("ur grade is 3")
elif 69>=x>=65:#2.5
 print("ur grade is 2.5")
elif 64>=x>=60:#2
 print("ur grade is 2")
elif 59>=x>=55:#1.5
 print("ur grade is 1.5")
elif 54>=x>=50:#1
 print("ur grade is 1")
elif 49>=x>=0:#congreatulation u must repeatedly study in class
 print("Congreatulation u must repeatedly study in class")
else :
 print("ur answer is error")