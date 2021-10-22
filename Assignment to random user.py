import random
people=[]
for x in range(0,8):
    person=input("Type the name of person : ")
    people.append(person)
index=random.randint(0,7)
r=people[index]
print("Random people is : ",r)