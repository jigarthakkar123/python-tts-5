d={901:"Aarav",877:"Hitesh",565:"Vishal",233:"Vihar",544:"Gaurang"}

print(d)
print(d[233])
d[233]="Parasar"
print(d)
for i in d:
    print(i," : ",d[i])
print(544 in d)
print(d.get(901))
print(d.items())
print(d.keys())
print(d.pop(565))
print(d)
print(d.popitem())
print(d)
d1={877:"Dolly",323:"Mahek",454:"Jaya"}
d.update(d1)
print(d)
