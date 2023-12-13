

def printName(name):
    print(name)

def printSkill(name,*skills):
    print(f"the name: {name}")
    for skill in skills:
        print(f"the skill is {skill}")


name= input("pleas enter your name: ").capitalize().strip()


s2=0
skills=[]
while s2 != 5:
       
   sk=input("Please enter yours skills: ").capitalize().strip()
   skills.append(sk)
   s2+=1



printSkill(name,skills)
