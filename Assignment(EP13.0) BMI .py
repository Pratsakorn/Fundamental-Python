#int ต้องมาก่อนinput
#โปรแกรมคำนวณหาค่าดัชนีมวลกาย
'''BMI=Weight(kg)/Hight^2(m)'''
#input str => float
Weight,hight=float(input("Your weight(Kg)\n")),float(input("Your hight(cm)\n"))
#process
#cm => m
Hight= (hight/100) '''hight/=100'''
#Calculate BMI
BMI = (Weight/(Hight**2))
#output
print ("Your BMI",BMI)