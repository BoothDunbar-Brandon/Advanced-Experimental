import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
import scipy

def norm(x, mean, std):
    norm=[]
    for i in range(len(x)):
        norm +=[(1.0/(std*np.sqrt(2*np.pi)))*np.exp(-(x[i] - mean)**2/(2*std**2))]
#    print norm
    return norm

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
###starts run 4 stuff
plt.plot(field4, counts4, 'b.')
error=[]
for count in counts4:
    x=math.sqrt(count)
    error.append(x)
#print error
print len(field4)
plt.errorbar(field4,counts4,yerr=error,fmt=None)
counts4=counts4[:27]
field4=sorted(field4)[22:]
print len(field4), counts4
#assert(False)
def model(t, coeffs):
    return coeffs[0]+ coeffs[1]*np.exp(-((t-coeffs[2])/coeffs[3])**2)

x0=np.array([17,120,1.67, 0.27],dtype=float)
x=np.linspace(1.25,2.0,100)
def residuals(coeffs,y,t):
    return y-model(t,coeffs)

from scipy.optimize import leastsq
x, flag= leastsq(residuals,x0, args=(counts4,field4))
print x, x0

plt.plot(field4, model(field4,x))
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Run 4')
plt.savefig('figure3.pdf')

#std1=counts4.std()
#mean1=counts4.mean()
#print mean1,std1
#ynorm= norm(counts4, mean1, std1)
#print ynorm, len(counts4), len(ynorm)
# plt.figure(4)
# plt.plot(field4,ynorm, '-')
# plt.savefig('test_gauss.pdf')
assert(False)

avg_field=[]
avg_count=[]
for point in range(0,len(field)):
    a=field[point]+field2[point]+field3[point]
    b=a/3
    avg_field.append(b)
    c=counts[point]+counts2[point]+counts3[point]
    d=int(c/3)
    avg_count.append(d)

plt.figure(4)
plt.plot(avg_field, avg_count,'.', color='cyan')
error=[]
for count in avg_count:
    x=math.sqrt(count)
    error.append(x)

plt.errorbar(avg_field,avg_count,yerr=error,fmt=None,ecolor='cyan')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.xlim(0.5,2.1)
plt.title('Average Runs 1-3')
plt.savefig('figure4.pdf')


std2=np.std(avg_count)
mean2=np.mean(avg_count)
print  mean2, std2

counts4_bg=[]
for point in range(0,len(counts4)):
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
