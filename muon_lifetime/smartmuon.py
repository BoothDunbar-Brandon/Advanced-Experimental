#Usage: type in terminal:
#	smartmuon.py "filename"

import matplotlib.pyplot as plt
import numpy as np
import LT.box as lt
import LT.MCA as M
import movingaverage as ma
import sys

#Gets Data from file
filename = sys.argv[1]
sp = M.MCA(filename)
counts = sp.cont
channels_original = sp.chn 

#Eliminate any values in the first 200 bins that are less than 10
edit = []
for i in range(0, 200):
	if counts[i] < 10:
		edit.append(i)
for i in edit:
	counts[i] = -1.

np.delete(counts, -1.)

#Eliminate any extreme values, larger data sets should allow stricter and more complicated
#function as filter paramaters, default moving average +- half moving average

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
	if counts[j] > ma_counts[j] - (ma_counts[j]/2)  or counts[j] < ma_counts[j] + (ma_counts[j]/2):
		counts1.append(counts[j])
		
#construct channels array that is the correct length
y = counts1.__len__()
channels = np.arange(0, y)

#Convert Channels to time using our calibration data
per_microsec = [204.85, 402., 608., 809.] 
microsec = np.arange(1, len(per_microsec) + 1)
calibration = np.mean(per_microsec / microsec)
timescale = channels / calibration

#Create 'Normalized' y-axis
normcounts = []
norm = np.sum(counts1)
for k in counts1:
	x = k * (1/norm)
	normcounts.append(x)

#Defines the parameters and initial guess values
lambda1 = lt.Parameter(0.5, 'Lambda1')
l1 = lt.Parameter(1., 'L1')
a1 = lt.Parameter( 1., 'A1')
b1 = lt.Parameter( 1., 'B1')
alpha1 = lt.Parameter( 0.4, 'Alpha1')
beta1 = lt.Parameter( 0.6, 'Beta1')

#Creates a fit for the 'ideal ratio' between positive and negative muons 
def ideal(x):
	return ( a1() * np.exp(-0.40*x) + b1() * np.exp(-0.60*x))
I = lt.genfit(ideal, [a1, b1], x = timescale, y = normcounts)

#Creates a single exponential fit
def single(x):
	return ( l1() * np.exp(-lambda1()*x))
L = lt.genfit(single, [l1, lambda1], x = timescale, y = normcounts)

#Performs two fits to find good starting values for the parameters 
def f1(x):
	return ( a1() * np.exp(-alpha1()*x))  
def f2(x):
	return ( b1() * np.exp(-beta1()*x))
F1 = lt.genfit(f1, [a1, alpha1], x = timescale, y = normcounts)
F2 = lt.genfit(f2, [b1, beta1], x = timescale, y = normcounts)

#Preserve data for fitting later if needed
a2 = a1.get()
b2 = b1.get()
alpha2 = alpha1.get()
beta2 = beta1.get()

#Final fit of our data
def f(x):
	return ( a1() * np.exp(-alpha1()*x) +b1() * np.exp(-beta1()*x))
F = lt.genfit(f, [a1, alpha1, b1, beta1], x = timescale, y = normcounts) 

#Define the values parameters in a better way, original is as tuplets
alpha1 = alpha1.get()
alpha1, alpha1r, err_alpha1  = alpha1[1], round(alpha1[1], 5), alpha1[2]
a1 = a1.get()
a1, a1r, err_a1 = a1[1], round(a1[1], 5), a1[2]

beta1 = beta1.get()
beta1, beta1r, err_beta1 = beta1[1], round(beta1[1], 5), beta1[2]
b1 = b1.get()
b1, b1r, err_b1 = b1[1], round(b1[1], 5), b1[2]

#Usually same value but not always
alpha2r, err_alpha2  = round(alpha2[1], 5), alpha2[2]
beta2r, err_beta2 = round(beta2[1], 5), beta2[2]

lambda1 = lambda1.get()
lambda1r, err_lambda1 = round(lambda1[1], 5), lambda1[2] 

#Plot 1 - Double Exponential Fit
fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(0, max(timescale))
plt.ylim(0, max(normcounts)+0.0002)

lt.plot_exp(timescale, normcounts,
	marker = '|', 
	color = 'grey',
	x_label = 'Decay Time  ($\mu s$)', 
	y_label = 'Number Density ($\%$ of total detected)',
	plot_title = 'Muon Decay, Double Exponential Fit'), 

lt.plot_line(I.xpl, I.ypl,
	linewidth = 1.5,
#	linestyle = '',
	color = 'b',
	label = r'Ideal Fit: $\alpha$ = 0.6000   $\beta$ = 0.4000')

lt.plot_line(F.xpl, F.ypl, 
	linewidth = 1.5,
#	linestyle = '',
	color = 'r',
	label = r'Data Fit: $\alpha$ = {0}   $\beta$ = {1}'.format(alpha1r, beta1r))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.savefig('graph_{0}_DbleExp.png'.format(filename))

#Plot 2 - Double v. Single Exponential Fit
fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(0, max(timescale))
plt.ylim(0, max(normcounts)+0.0002)

lt.plot_exp(timescale, normcounts,
	marker = '|',
	color = 'grey', 
	x_label = 'Decay Time  ($\mu s$)', 
	y_label = 'Number Density ($\%$ of total detected)',
	plot_title = 'Muon Decay, Double vs. Single Exponential Fit'), 

lt.plot_line(F.xpl, F.ypl, 
	linewidth = 1.5,
#	linestyle = '',
	color = 'b',
	label = r'Double Exponential: $\alpha$ = {0}   $\beta$ = {1}'.format(alpha1r, beta1r))

lt.plot_line(L.xpl, L.ypl,
	linewidth = 1.5,
#	linestyle = '',
	color = 'r',
	label = r'Single Exponential: $\lambda$ = {0}'.format(lambda1r))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.savefig('graph_{0}_DbleVSnglExp.png'.format(filename))

#Plot 3 - Each part of the fit
fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim(0, max(timescale))
plt.ylim(0, max(normcounts)+0.0002)

x = timescale

def final1(x):
	return ( a1 * np.exp(-alpha1*x))

def final2(x):
	return ( b1 * np.exp(-beta1*x))

lt.plot_exp(timescale, normcounts,
	marker = '|', 
	color = 'grey',
	x_label = 'Decay Time  ($\mu s$)', 
	y_label = 'Number Density ($\%$ of total detected)',
	plot_title = 'Muon Decay, Positive and Negative Muon Contributions'), 


lt.plot_line(F.xpl, F.ypl, 
	linewidth = 1.5,
	linestyle = '--',
	color = 'r',
	label = r'Double Exponential: $\alpha$ = {0}   $\beta$ = {1}'.format(alpha1r, beta1r))

plt.plot(x, final1(x), 
	linewidth = 1.5,
	color = 'g',
#	linestyle = '--',
	label = r'Positive Muon Exponential: $\lambda_+$ = {0}'.format(alpha1r))

lt.plot_line(x, final2(x), 
	linewidth = 1.5,
#	linestyle = '--',
	color = 'b',
	label = r'Negative Muon Exponential: $\lambda_-$ = {0}'.format(beta1r))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.savefig('graph_{0}_CompExp.png'.format(filename))


