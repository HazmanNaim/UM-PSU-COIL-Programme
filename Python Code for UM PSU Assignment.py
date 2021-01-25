'''

This code is intended for assignment purpose under COIL programme

'''
import matplotlib.pyplot as mpl
import pandas as pd
from scipy.stats import linregress
#import necessary mpackages

'''
1) READ THE DATA FROM EXCEL
'''
#Instruct 'Panda' to read the data from external file
#In this case, the data is written in the excel sheet
#Write the name of the file, in this case, the name of the file is 'Linear Regression Data.xlsx'
dataframe = pd.read_excel('Linear Regression Data.xlsx')

#The Data must be assigned to its corresponding X and Y variable
x = dataframe.Distance
y = dataframe.Intensity


'''
2) Calling the linregress from scipy.stats package
'''
#Write this in the code, othwerwise the code do not know what we are doing ((Confused screaming)
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
#'mpl.scatter' is plotting individual values (For experimental data, we take discrete measurements)
#'mpl.plot' is plotting continuous values 
mpl.scatter(x,y, s=10 ,label='Experimental Data')
mpl.plot(x, m*x + b, label='Linear Regression') #That's why we introduce m and b variables earlier (At line 34 and 35)


'''
5) Graph Labelling
'''
#labelling for the Plots
mpl.xlabel('Distance^-2') #The X data is '1/distance squared'
#mpl.xlabel('$1/(Distance^2)$ [$m^{-2}$]')                #This one is fancier hehe (I use LateX format), you can replace the line 50 with this one but it is optional
mpl.ylabel('Intensity') #The Y data is 'Intensity'
mpl.title('Graph of Light Intensity against 1/d^2')
mpl.axvline(0,color='Black') #axv and axh are both for drawing black lines for the axis (Optional)
mpl.axhline(0,color='Black')

'''
6) Print the information/result from the linear regression 
'''
#I just improve this part to make it more 'understandable'

print("-------------Basic Information(s)-------------")
print("The R-squared value is: ", lslinear.rvalue**2 , "        (How close the data are to the fitted regression line)")
print("The Gradient of the graph is: ", m , "        (Gradient of the regression line)")
print("The Y-Intercept of the graph is: ", b , "        (Intercept of the regression line)")
print("----------------------------------------------")

'''
7) Export the Plot in png/jpeg format
'''
# Save the graph in the png format in an external file.
mpl.savefig("Plot.png")

'''
8) To show the plot
'''
#These two are important
mpl.legend()
mpl.show()

#You can add more parameter like 'Standard Error of the Gradient' by writing "lslinear.stderr"
#Example below:
#Del_m = lslinear.stderr






