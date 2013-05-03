import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

r1=(2.30+2.70)/2
def f(Y):
    a=Y/np.sqrt(Y**2+r1**2)
    b=r1**2/(Y**2+r1**2)
    X=7.22
    return a*b/np.sin(0.5*(np.arctan(r1/X)+np.arctan(r1/Y)))**4
Y=np.arange(0,20,.01)
print max(f(Y))

length=np.arange(3,18.5,0.5)
print length

counts=[1551,1487,1519,1604,1633,1705,1650,1752,1660,1791,1783,1845,1843,1925,1867,1869,1936,1838,1838,1741,1748,1730,1787,1513,1460,1217,1218,985,847,632,465]
print max(counts)

counts2=[x/218. for x in counts]
error=np.sqrt(counts)/218.
print np.sqrt(counts)
plt.plot(length,counts2)
plt.errorbar(length, counts2, yerr=error,fmt='.',ecolor='blue')
popt,pcov=scipy.optimize.curve_fit(f,length,counts2)
plt.xlim(0,20)
plt.xlabel('Y (cm)')
plt.ylabel('f(Y)')
plt.show()
