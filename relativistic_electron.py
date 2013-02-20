import csv
import matplotlib.pyplot as plt

#c=open("relativistic_electron.csv", "rb")
c=open("data.txt", "r")
d=c.readlines()
c.close()
x=[]
y=[]
for line in d:
    a=line.split()
    print a
    x.append(float(a[0]))
    y.append(float(a[1]))
    break
print x,y
plt.plot(x,y)
plt.xlabel('B field (kG)')
plt.ylabel('Counts/5 min')
plt.show()

#add error bars for B field

"""first column is B field in kG, second is # of counts/5 min 
|error margin in kG is +/-.0002
|Amplifier - fine = 9.5, coarse = 20   then discriminator Delta E = 0.5 V"""
