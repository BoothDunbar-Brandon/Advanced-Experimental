import numpy as np
import matplotlib.pyplot as plt

#given in manual
r1=(2.30+2.70)/2


def f(Y):
    a=Y/np.sqrt(Y**2+r1**2)
    b=r1**2/(Y**2+r1**2)
    X=7.22
    return a*b/np.sin(0.5*(np.arctan(r1/X)+np.arctan(r1/Y)))**4

Y=np.arange(1,20,0.01)
plt.plot(Y,f(Y))
plt.xlabel('Y (cm)')
plt.ylabel('f(Y)')
plt.savefig('preliminary_plot.pdf')
#plt.show()
