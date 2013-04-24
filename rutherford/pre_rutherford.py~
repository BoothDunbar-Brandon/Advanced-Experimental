import numpy as np
import matplotlib.pyplot as plt

#given in manual
r1=(2.30+2.70)/2

#retrieve values for theta1 which changes as we change Y
def theta1(Y):
    return (1/np.arctan(Y/r1))

Y=np.arange(0,20,0.01)
Y=theta1(Y)

#fixed number from geometry of setup
theta2=np.arcsin(r1/7.22)
print theta2


def func(theta1):
    return np.cos(theta2)*(np.sin(theta2))**2/(np.sin((theta1+theta2)/2))**4

print func(Y)
print theta1(Y)
#this should really be plotting Y vs, f(Y) since theta is a function of Y
plt.plot(Y,func(Y))
#plt.xlim(0,20)
#plt.ylim(0,100000)
plt.xlabel('Y (cm)')
plt.ylabel('f(Y)')
plt.show()
