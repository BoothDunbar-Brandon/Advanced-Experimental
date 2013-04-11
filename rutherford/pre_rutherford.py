import numpy as np
import matplotlib.pyplot as plt

r1=(2.30+2.70)/2

def theta1(Y):
    return (1/np.arctan(Y/r1))

Y=np.arange(0,20,0.01)
Y=theta1(Y)

theta2=np.arcsin(r1/7.22)
print theta2

def func(theta1):
    return np.cos(theta2)*(np.sin(theta2))**2/(np.sin((theta1+theta2)/2))**4

print func(Y)

print theta1(Y)
#assert(False)
plt.plot(Y,func(Y))
#plt.xlim(0,20)
#plt.ylim(0,100000)
plt.xlabel('Y (cm)')
plt.ylabel('f(Y)')
plt.show()
