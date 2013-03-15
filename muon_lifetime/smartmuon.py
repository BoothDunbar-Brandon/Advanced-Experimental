import matplotlib.pyplot as plt
import numpy as np
import LT.box as lt
import LT.MCA as M


#Gets Data
sp = M.MCA('EPBB1.Spe')

#Defines Data 
counts = sp.cont
channels = sp.chn


#Defines the parameters and initial guess values
a1 = lt.Parameter( 10., 'A1')
b1 = lt.Parameter( 10., 'B1')
alpha1 = lt.Parameter( 0.3, 'Alpha1')
beta1 = lt.Parameter( 0.7, 'Beta1')

#Fit each function individually then use the fit values as the starting values for the final fit. 

def f1(x):
    return ( a1() * np.exp(-alpha1()*x)) 


F1 = lt.genfit(f1, [a1, alpha1], x = channels, y = counts) 

def f2(x):
    return ( b1() * np.exp(-beta1()*x)) 


F2 = lt.genfit(f2, [b1, beta1], x = channels, y = counts)



def f(x):
    return ( a1() * np.exp(-alpha1()*x) +b1() * np.exp(-beta1()*x)) 

#defines fit parameters in terms of function and data
F = lt.genfit(f, [a1, alpha1, b1, beta1], x = channels, y = counts) 


#Creates a plot of the array instead of a histogram
lt.plot_exp(channels, counts)
#

#plots fit line, doesn't take color argument, ew. 
lt.plot_line(F.xpl, F.ypl)

t = map(f, channels)
plt.plot(channels, t, 'r')


plt.xlim(0, 2048)
plt.ylim(0, 80)

plt.show()
