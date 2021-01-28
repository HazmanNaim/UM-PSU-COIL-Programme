'''
LEAST-SQUARES FITTING
'''
#import necessary packages/libraries
import matplotlib.pyplot as mpl
import pandas as pd
from scipy.stats import linregress
'''
1) READ THE DATA FROM EXCEL
'''
#Instruct 'Panda' to read the data from external file
#In this case, the data is written in the excel sheet
#Write the name of the file, in this case, the name of the file is 'Linear Regression Data.xlsx'
dataframe = pd.read_excel('Linear Regression Data.xlsx')

#The Data must be assigned to its corresponding X and Y variable
x = dataframe.X
y = dataframe.Y
'''
2) Calling the linregress from scipy.stats package
'''
lslinear = linregress(x,y)
'''
3) Calculate the Slope and Intercept
'''
#We want the code to calculate the slope and the intercept for the linear regression
m = lslinear.slope
b = lslinear.intercept
'''
4) Plotting the Experimental Data and Linear Regression
'''
mpl.scatter(x,y, s=10 ,label='Experimental Data', color = 'Black')
mpl.plot(x, m*x + b, label='Linear Regression', color = 'Red')
'''
5) Graph Labelling
'''
#labelling for the Plots
mpl.xlabel('$1/(d^2)$ [$m^{-2}$]')         #The X data is '1/distance squared'
mpl.ylabel('Intensity,$I$ [Lux]') #The Y data is 'Intensity'
mpl.title('Graph of \n Light Intensity against $1/(d^2)$')
mpl.axvline(0,color='Black') #axv and axh are both for drawing black lines for the axis (Optional)
mpl.axhline(0,color='Black')
'''
6) Print the information/result from the linear regression 
'''
print("-------------Basic Information(s)-------------")
print("The R-squared value is: ", lslinear.rvalue**2 , "  (How close the data are to the fitted regression line)")
print("The Gradient of the graph is: ", m , "  (Gradient of the regression line)")
print("The Y-Intercept of the graph is: ", b , "  (Intercept of the regression line)")
print("----------------------------------------------")
'''
9) To show the plot
'''
#These two are important
mpl.legend()
mpl.show()
'''
END
'''






