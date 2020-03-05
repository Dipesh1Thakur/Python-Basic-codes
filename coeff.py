import numpy as np
import matplotlib.pyplot as plt
from numpy import mean
x = np.array(range(1,14))
y = np.array([2,8,8,18,25,21,32,44,32,48,61,45,62])

# a = (mean(x)*mean(y)-mean(x*y)) / (mean(x)**2 - mean(x**2))
# b= mean(y)- a*mean(x)
[a,b] = np.polyfit(x,y,1)
plt.plot(0,21),[b,21*a+b],'r--s'

plt.scatter(x,y)
plt.scatter(20,20*a+b),color='green'
plt.show()
