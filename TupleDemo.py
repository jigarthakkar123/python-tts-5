t=(10,20,"tops",True,[100,200,300],1,2,1.1,"Python")

print(t)
print(t.count(1))
print(t.index(1))

for i in t:
    print(i)

print(22 in t)
print(t[4])
t[4].append(400)
print(t)
