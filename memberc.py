# membership simple example

adminList=["Hamza","Osama","Ahmad","Sami"]

adminName=input("Enter Admin Name: ").strip().capitalize()
if adminName in adminList:
    print(f"Wlcome {adminName} in Admin Cpanel")
    action=int(input("please chouse your action : 1-Rename 2-Delete: "))
    if action ==1:
        newName=input("Please Enter New Name: ").strip().capitalize()
        adminList[adminList.index(adminName)]=newName
        print(adminList)
    elif action ==2:
        adminList.remove(adminName)
        print(adminList)
    else:
        print("wroing Chouse")

else:
    print("You Are not Admin")    