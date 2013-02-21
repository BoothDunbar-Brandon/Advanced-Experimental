import csv
import matplotlib.pyplot as plt
import numpy as np

field,counts, field2, counts2=np.loadtxt("data.txt", skiprows=0, unpack=True)
print field
plt.plot(field,counts, 'o-')
plt.plot(field2,counts2, 'o-')
plt.xlabel('B field (kG)')
plt.ylabel('Counts/ 5 min')
plt.show()

#add error bars for B field

"""first column is B field in kG, second is # of counts/5 min 
|error margin in kG is +/-.0002
|Amplifier - fine = 9.5, coarse = 20   then discriminator Delta E = 0.5 V"""
