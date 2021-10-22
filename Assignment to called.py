person={"name" : "Pratsakorn", 
        "gender" : "Male", 
        "age" : "17", 
        "address" : "Cybertron", 
        "phone" : "012-345-6789"}
key = (input("Tell me what do u want to know : ")).lower()#ใส่lowerเพื่อป้องกันการ case sensitive(ตัวล่างเล็กแล้วต้องทำบนให้เล็กด้วย)
result = person.get(key,"This information is not avaliable")
print(result)