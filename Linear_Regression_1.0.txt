#Linear regression in python
#y = ax + b
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

a = 0
b = 0
c = 0
d = 0

#Import .xls file
xls = pd.read_excel (r'C:\Users\Arno\Desktop\Test_python.xls')
#print(xls)

#Table size
size = len(xls)
#print('Table size: ', size)

#Calculate the average of each set
avg_x = sum(xls.iloc[:,0])/size
avg_y = sum(xls.iloc[:,1])/size


#Nominator of a
#(Xi - Xavg)*(Yi-Yavg)
for i in range(size):
    a = xls.at[i,0] - avg_x
    b = xls.at[i,1] - avg_y
    c += a*b
    
#Denominator of a
#(Xi-Xavg)^2    
for i in range(size):
    d += (xls.at[i,0] - avg_x)**2
    
#Define a
a = c/d

#Define b
b = avg_y - a*avg_x

x = []
y = []

for i in range(size):
    x.append(xls.at[i,0])
    y.append(xls.at[i,1])

   
#'o' means we plot dots
plt.plot(x,y,'o')

#The regression line
xr = np.arange(xls[0].min(),xls[0].max(),(xls[0].max()-xls[0].min())/size)
yr = a * xr + b
plt.plot(xr,yr)
