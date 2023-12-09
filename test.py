# the first test programming by python

myString= "******** i love python lang *******"

print(len(myString))
print(myString.strip("* "))
print(myString.strip("* ").title())
myString2= "i-love-pYTHon-and-php-and-msql"
print(myString2.rsplit("-",2))
print(myString2.center(50,"*"))
print(myString2.swapcase())
print(myString.strip("*"))
li=myString.strip("*").split()
print(li[0].center(10,"@"))
print(li)
print(len(myString))
my4="@".join(li)
print(my4)