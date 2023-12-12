myList=["Hamza","Zaki","Obaydallah","Sabha","Sobheaa"]
print(myList[0])
a=0
while a<len(myList):
    print(f"#{str(a+1).zfill(2)} {myList[a]}")
    a+=1
    if a==4 :
        break
