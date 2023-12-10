s={1,3,"tr",True,"hamza"}
t={4,7,2,"sofia","rr"}
print(s)
print(t)
s.add("has")
print(s)
r=s.copy()
print(r)
b=s.union(t)
print(b)
t.remove("sofia")
t.discard("rr")

print(t)
t.clear()
print(t)
