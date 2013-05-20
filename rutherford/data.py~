import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

r1=(2.30+2.70)/2
def f(Y):
    a=Y/np.sqrt(Y**2+r1**2)
    b=r1**2/(Y**2+r1**2)
    X=7.22
    return a*b/np.sin(0.5*(np.arctan(r1/X)+np.arctan(r1/Y)))**4
Y=np.arange(0.01,20,.01)
print max(f(Y))

length1=np.arange(3,19,1.0)
length2=np.arange(3,18.5,0.5)
counts1=[1551,1519,1633,1650,1660,1783,1843,1887,1936,1838,1748,1727,1460,1218,847,465]
counts2=[1551,1487,1519,1604,1633,1705,1650,1752,1660,1791,1783,1845,1843,1925,1887,1869,1936,1838,1838,1761,1748,1730,1727,1513,1460,1217,1218,985,847,632,465]
counts1=counts1[::-1]
counts2=counts2[::-1]

plt.figure(1)
plt.plot(length1,counts1,'-o', color='purple')

plt.xlim(0,20)
plt.ylim(0,2000)
plt.xlabel('Y (cm)')
plt.ylabel('Counts/20 minutes')
plt.savefig('firstrun.pdf')

plt.figure(2)
plt.plot(length2,counts2,'-o', color='red')
plt.xlim(0,20)
plt.ylim(0,2000)
plt.xlabel('Y (cm)')
plt.ylabel('Counts/20 minutes')
plt.savefig('secondrun.pdf')


plt.figure(3)
def N(count,length):
    return count/((8.932e-6)*f(length))

print N(counts2,length2)
N0=np.mean(N(counts2,length2))
print N0, np.std(N(counts2,length2))

assert(False)
def N2(length):
    return (8.932e-6)*N0*f(length)
print len(N2(length2))

plt.plot(Y,N2(Y),'r-',label=r'Calculated $N_2$')
length2=length2-2.
print length2
print np.mean(N2(Y))
#plt.plot(length2,counts2,'bo')
plt.errorbar(length2, counts2, yerr=np.sqrt(counts2), xerr= 0.1, fmt='b.',ecolor='blue', label=r'experimental $N_2$')
plt.xlabel('Y (cm)')
plt.ylabel('Counts/20 minutes')
plt.legend(loc=4)
plt.savefig('N2.pdf')


plt.show()




#popt,pcov=scipy.optimize.curve_fit(f,length,counts2)
plt.show()
