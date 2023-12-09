# List 
myList=[1,4,"one", "three", True]
print(myList)
print(myList[2])
print(myList[0:3])
myList[2]= "Hamza"
print(myList)
myList[1:3]= ["Hamza"]
print(myList)

#List Methods
myList2=[1,3,5,2,6,7]
myList3=["A","Z","T","K"]
#myList2.append(100)
#print(myList2)
#myList2.append(myList3)
#print(myList2)
#myList2.extend(myList3)
#print(myList2)
myList2.sort()
print(myList2)
myList3.remove("T")
print(myList3)
myList.insert(1,"ggg")
print(myList)
print(myList.count("ggg"))
