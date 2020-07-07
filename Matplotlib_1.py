# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:50:10 2020

@author: moham
"""
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

#LINE PLOTS
print(plt.style.available) #shows different avaiable matplotlib built-in styles
plt.style.use('fivethirtyeight')
#plt.xkcd() #a fun style similar to xkcd comics website. This is a method.

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color= 'k', linestyle= '--', marker='.', label='All Devs') #creates the plot, with a 
#label for the legend, 'k' is 'black' for the line color, and '.' as marker and '--' the line style.
#py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]#median salaries for Python developers

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]#median salaries for Java developers

plt.plot(ages_x, py_dev_y, color='b', label='Python')

##Another way of color codes are HEX values that codes can be found online. for example:

plt.plot(ages_x, py_dev_y, color='#5a7d9a',linewidth=3, label='Python') #linewidth modified to look thicker. default is 1.
plt.plot(ages_x,js_dev_y, color='#adad3b', linewidth=3, label ='Javascript')
plt.plot(ages_x, dev_y, color= '#444444', linestyle= '--', marker='.', label='All Devs')
#the order tells python which line would be on top. Here the all developers dotted line is last 
#so that it becomes more visible on top of the thick Javascript line.

##Styles: if different built-in styles are used, I can remove the colors and linewidth to check
#whether the default of the style looks better. May also remove the grids:
plt.plot(ages_x, py_dev_y, color='#5a7d9a',linewidth=3, label='Python') #linewidth modified to look thicker. default is 1.
plt.plot(ages_x,js_dev_y, label ='Javascript')
plt.plot(ages_x, dev_y, marker='.', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')
##plt.legend(['All Devs', 'Python']) #adds legend to the plot using a list. First item 
#in the list refers to the first plot line, and second to the second line.
#another way to add legends is adding labels to the plt.plot and just use plt.legend()
plt.legend()
plt.tight_layout() #adjusts subplot padding parameters
plt.grid(True)#adding a grid for better visuals

plt.savefig('plot.png') #saves the plot in png format in the current directory.
plt.show() #shows the plot 

##BAR CHARTS
plt.style.use('fivethirtyeight')
plt.bar(ages_x, dev_y, color= '#444444', label='All Devs')

#Now let's create a bar chart for the 3 different graphs in previous part (all devs, python, java).
#

x_indexes = np.arange(len(ages_x)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.25 #defining the value that is going to be used as width of bars
plt.bar(x_indexes - width, dev_y, width = width, color='#444444', label='All Devs')
plt.bar(x_indexes,js_dev_y, width = width, color='#e5ae38',label ='Javascript')
plt.bar(x_indexes + width, py_dev_y, width = width, color='#5a7d9a', label='Python')


plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x) #replaces the indexes with the ages on X axis.

plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.title('Median Salary (USD) by Age')

plt.tight_layout()
plt.show()

##SUB PLOT
df = pd.read_csv('data_1.csv') 
plt.gcf()
plt.gca()
plt.style.use('seaborn')
ages = df['Age']
py_salaries = df['Python']
dev_salaries = df['All_Devs']
js_salaries = df['JavaScript']
fig, ax = plt.subplots(nrows=2, ncols=1) #subplots create a figure and then specify a certain number of axis. 
#If not specified, default would be 1 row, 1 column, so 1 axis.
print(ax)
ax.plot(ages, py_salaries, label = 'Python')
ax.plot(ages, js_salaries, label = 'JavaScript')
ax.plot(ages, dev_salaries, color= '#444444', linestyle='--', label = 'All Devs')

ax.legend()

ax.set_title('Median Salary(USD) by Age')
ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
