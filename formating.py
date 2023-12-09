# formatting old way

name="hamza"
age=36
salary=6000
print("Iam %s my ag is: %.2f with salary: %d" %(name,age,salary))

# formatting new way

n="hamza"
age=36
salary=9000
print("iam {:.2s} my age is: {:d} with salary: {:.2f}".format(n,age,salary))

#formatting new way 3.6 +

n1="hamza"
age1=36
salary1=9000

print(f"iam {n1:.2s} my age is: {age1} with salary: {salary:.4f}" )