import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math

field,counts, field2, counts2, field3, counts3=np.loadtxt("data.txt", skiprows=0, unpack=True)
field4, counts4= np.loadtxt("data2.txt", skiprows=0, unpack=True)

plt.figure(1)
plt.plot(field,counts, 'r.')
plt.plot(field2,counts2, 'k.')
plt.plot(field3,counts3, 'g.-')
plt.plot(field4, counts4, 'b.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.title('All Raw Data')
plt.xlim(0.5,2.1)
plt.savefig('figure1.pdf')

plt.figure(2)
plt.plot(field,counts, 'r.')
plt.plot(field2,counts2, 'k.')
plt.plot(field3,counts3, 'g.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Runs 1-3')
plt.savefig('figure2.pdf')

plt.figure(3)
plt.plot(field4, counts4, 'b.')
error=[]
for count in counts4:
    x=math.sqrt(count)
    error.append(x)
print error
plt.errorbar(field4,counts4,yerr=error,fmt=None)
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Run 4')
plt.savefig('figure3.pdf')

plt.figure(4)
avg_field=[]
avg_count=[]
for point in range(0,len(field)):
    a=field[point]+field2[point]+field3[point]
    b=a/3
    avg_field.append(b)
    c=counts[point]+counts2[point]+counts3[point]
    d=c/3
    avg_count.append(d)

plt.plot(avg_field, avg_count,'.', color='cyan')
error=[]
for count in avg_count:
    x=math.sqrt(count)
    error.append(x)
print error
plt.errorbar(avg_field,avg_count,yerr=error,fmt=None,ecolor='cyan')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Average Runs 1-3')
plt.savefig('figure4.pdf')
assert(False)
counts4_bg=[]
for point in range(0,len(field4)):
    x=counts4[point]-17.8
    counts4_bg.append(x)
print counts4,counts4_bg

plt.figure(5)
plt.plot(field4, counts4_bg, 'b.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Run 4 Minus Background')
plt.savefig('figure5.pdf')

avg_count_bg=[]
for point in range(0,len(avg_field)):
    x=avg_count[point]-17.8
    avg_count_bg.append(x)
print avg_count[1], avg_count_bg[1]

plt.figure(6)
plt.plot(avg_field, avg_count_bg, '.', color='cyan')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Average Runs 1-3 Minus Background')
plt.savefig('figure6.pdf')

#assert(False)



#make large page of 6 subplots
plt.subplots_adjust(wspace=0.4, hspace=0.5)
matplotlib.rcParams['font.size']=8
#print field
plt.subplot(321)
plt.plot(field,counts, 'r.')
plt.plot(field2,counts2, 'k.')
plt.plot(field3,counts3, 'g.')
plt.plot(field4, counts4, 'b.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.title('Fig 1: All Raw Data')
plt.xlim(0.5,2.1)

plt.subplot(322)
plt.plot(field,counts, 'r.')
plt.plot(field2,counts2, 'k.')
plt.plot(field3,counts3, 'g.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Fig 2: Average of Runs 1-3')

plt.subplot(323)
plt.plot(field4, counts4, 'b.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Fig 3: Run 4')

plt.subplot(324)
plt.plot(avg_field, avg_count, '.', color='cyan')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Fig 4: Average Runs 1-3')

plt.subplot(325)
plt.plot(field4, counts4_bg, 'b.')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Fig 5: Run 4 Minus Background')

plt.subplot(326)
plt.plot(avg_field, avg_count_bg, '.', color='cyan')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Fig 6: Average Runs 1-3 Minus Background')


plt.savefig('field_counts.pdf')
plt.legend()


    
#add error bars for B field

"""first column is B field in kG, second is # of counts/5 min 
|error margin in kG is +/-.0002
|Amplifier - fine = 9.5, coarse = 20   then discriminator Delta E = 0.5 V
background for 5 min- 16, 19, 14, 17, 19, 20----avg=17.8"""
