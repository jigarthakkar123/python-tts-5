l=[]

for i in range(1000,3001):
    if i%5==0 and i%7!=0:
        l.append(i)
print(l)
