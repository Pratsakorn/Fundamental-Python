weight, height =float(input("Tell me your weight(kg) :")), float(input("Tell me your height(meter) :"))
BMI = weight/(height**2)
print("Your BMI :", round(BMI,2))
if   (BMI<=18.5):
    print("Underweight")
elif (24.9>=BMI>18.5):
    print("Normal weight")
elif (29.9>=BMI>24.9):
    print("Overweight")
elif (BMI>=30):
    print("Obesity")