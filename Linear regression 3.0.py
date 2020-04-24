#Linear regression in python where you get to chose wich column
#y = ax + b
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

a = 0
b = 0
c = 0
d = 0
e = 0

#Import .xls file
xls = pd.read_excel (r'D:\test2.0.xlsx')

#Define 
row = xls.shape[0]
col = xls.shape[1]

#First row is considered as title
print('You have ', row, 'rows.')
print('You have ', col, 'columns.')

#Choosing columns
x = int(input('Enter the index of the first columns '))
print('You chose the column ', x)
y = int(input('Enter the index of the second columns '))
print('You chose the column ', y)

x = 1
y = 2

#Calculate the average of X and Y columns
avg_x = sum(xls.iloc[:,x])/col
avg_y = sum(xls.iloc[:,y])/col

#Nominator of the slope (Xi - Xavg)*(Yi-Yavg)
for i in range(col-1):
    a = xls.iat[i,x] - avg_x
    b = xls.iat[i,y] - avg_y
    c += a*b

#Covariance (Xi - Xavg)*(Yi-Yavg)/N
covar = c/col

#Denominator of the slope #(Xi-Xavg)^2    
for i in range(col-1):
    d += (xls.iat[i,x] - avg_x)**2
    e += (xls.iat[i,y] - avg_y)**2

#Standard deviation (Xi - Xavg)²/N
sdx = (d/col)**0.5
sdy = (e/col)**0.5
    
#Define a
a = c/d

#Define b
b = avg_y - a*avg_x

#reframing dataset
xf = []
yf = []
for i in range(col-1):
    xf.append(xls.iat[i,x])
    yf.append(xls.iat[i,y])

#Correlation
r=0
r = covar*(sdx*sdy)**-1

print('Covariance is ',covar)
print('Standard deviation of X ', sdx)
print('Standard deviation of Y ', sdy)
print('Correlation is ', r)
