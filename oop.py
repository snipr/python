# OOP Learning
class pirson:
    mName="hamza zaki"
    @classmethod
    def printmName(cls):
        return f"the m name=: {cls.mName}"

    def __init__(self,name,age,staudy):

        self.name=name
        self.age=age
        self.staudy=staudy

    def gitInfo(self):
        return f"the name is: {self.name} and the age is: {self.age} and the study is: {self.staudy}"
    
class human(pirson):

    def __init__(self,name,age,staudy):
       super().__init__(name,age,staudy)


       
name=input("Enter your name: ")
age=input("enter your age: ")
staudy=input("enter your study: ")

jj=pirson(name,age,staudy)

print(jj.gitInfo())

print(f"{pirson.printmName()}")

print(f"{human('hasan',55,'it').gitInfo()}")
        