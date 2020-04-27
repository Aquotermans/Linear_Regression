#Linear regression in python where you get to chose wich column
#y = ax + b
import seaborn as sns
import pandas as pd

a = 0
b = 0
c = 0
d = 0
e = 0

#Import .xls file
xls = pd.read_excel (r'D:\titanic.xlsx')

#Define 
row = xls.shape[0]
col = xls.shape[1]
size = len(xls)

#First row is considered as title
print('You have ', row, 'rows.')
print('You have ', col, 'columns.')

#Choosing columns
x = int(input('Enter the index of the first columns '))
print('You chose the column ', x)
y = int(input('Enter the index of the second columns '))
print('You chose the column ', y)


#Calculate the average of X and Y columns
avg_x = sum(xls.iloc[:,x])/size
avg_y = sum(xls.iloc[:,y])/size


#Nominator of the slope (Xi - Xavg)*(Yi-Yavg)
for i in range(size):
    a = xls.iat[i,x] - avg_x
    b = xls.iat[i,y] - avg_y
    c += a*b


#Covariance (Xi - Xavg)*(Yi-Yavg)/N
covar = c/size

#Denominator of the slope #(Xi-Xavg)^2    
for i in range(size):
    d += (xls.iat[i,x] - avg_x)**2
    e += (xls.iat[i,y] - avg_y)**2
   

#Standard deviation (Xi - Xavg)²/N
sdx = (d/row)**0.5
sdy = (e/row)**0.5
    
#Define a
a = c/d

#Define b
b = avg_y - a*avg_x

#reframing dataset
xf = []
yf = []
for i in range(row-1):
    xf.append(xls.iat[i,x])
    yf.append(xls.iat[i,y])
    
df = list(zip(xf, yf))   
df = pd.DataFrame(df)

#Correlation
r=0
r = covar*(sdx*sdy)**-1

#Change format
covar = "{:.3f}".format(covar)
sdx = "{:.3f}".format(sdx)
sdy = "{:.3f}".format(sdy)
r = "{:.3f}".format(r)

print('Covariance is ',covar)
print('Standard deviation of X ', sdx)
print('Standard deviation of Y ', sdy)
print('Correlation is ', r)

sns.pairplot(df)
