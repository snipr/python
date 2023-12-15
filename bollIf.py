hello=lambda name,age: f"name is {name} and age {age}"

print(hello("hamza",36))

myList=["Hamza","zaki","ahmad","mosa"]

def names(name):
    return f"-- {name}--".capitalize().strip()

newList=map(names,myList)

for n in newList:
    print(n)