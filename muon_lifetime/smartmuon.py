import matplotlib.pyplot as plt
import numpy as np
import LT.box as lt
import LT.MCA as M
import movingaverage as ma

#Gets Data
sp = M.MCA('EPBB1.Spe')

#Defines Data count
counts = sp.cont
channels = sp.chn 
#Eliminate the first couple values from the beggining of the list 'counts'

edit = []

for i in range(0, 100):
	if counts[i] < 40:
		counts.del(i)

#for i in edit:
#	counts[i] = '!'

#for i in range(0,counts.count('!')):
#	counts.remove('!')



#Need to eliminate extreme values in the data set which are skewing the fit.
#create a list of moving averages
ma_counts = ma.movingaverage(counts, 10)

#make realcounts and counts the same length by adding zeros to the end of the list
a = ma_counts.__len__()
b = counts.__len__()
c = b - a
zeros = [0] * c
ma_counts.extend(zeros) 

counts1 = []

for j in range(0, len(counts)):
	if counts[j] > ma_counts[j] - 10 or counts[j] < ma_counts[j] + 10:
		counts1.append(counts[j])
		

#construct channels array that is the correct length
y = counts1.__len__()
channels = np.arange(0, y)

#Defines the parameters and initial guess values
a1 = lt.Parameter( 100., 'A1')
b1 = lt.Parameter( 100., 'B1')
alpha1 = lt.Parameter( 0.4, 'Alpha1')
beta1 = lt.Parameter( 0.6, 'Beta1')

#Fit each function individually then use the fit values as the starting values for the final fit, F. 
def f1(x):
	return ( a1() * np.exp(-alpha1()*x)) 

F1 = lt.genfit(f1, [a1, alpha1], x = channels, y = counts1) 

def f2(x):
	return ( b1() * np.exp(-beta1()*x)) 

F2 = lt.genfit(f2, [b1, beta1], x = channels, y = counts1)

def f(x):
	return ( a1() * np.exp(-alpha1()*x) +b1() * np.exp(-beta1()*x)) 

F = lt.genfit(f, [a1, alpha1, b1, beta1], x = channels, y = counts1) 


#Creates a plot of the array instead of a histogram
lt.plot_exp(channels, counts1)

#plots spectrum
#ax1 = lt.get_spectrum('EPBB1.Spe')
#ax1.plot()

#plots fit line. 
lt.plot_line(F.xpl, F.ypl, color='r')

plt.xlim(0, 2048)
plt.ylim(0, 80)

plt.show()
