l=[1,2,10,"python",False,"Java",101,202,303,1,2,3,1.1,2.2,10,"tops",True]
l1=[]


for i in l:
    print(i)
print(10.10 in l)

for i in l:
    c=l.count(i)
    if c>1:
        if i not in l1:
            l1.append(i)
print(l1)
