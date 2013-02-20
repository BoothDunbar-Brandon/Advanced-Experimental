import csv

c=open("relativistic_electron.csv", "rb")
d=c.readlines()
x=[]
y=[]
for line in d:
    a=line.split()
    print a
    x.append(float(a[0]))
    y.append(float(a[1]))
print x,y
