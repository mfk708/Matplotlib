# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:22:31 2020

@author: moham
"""
from matplotlib import pyplot as plt
import csv
import numpy as np
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#row = next(csv_reader) : chooses the first row of the csv file and assigns it to 'row'.
#print(row['LanguagesWorkedWith'].split(';')): splits the items in the row from ; and prints them.
language_counter = Counter()
    
for row in csv_reader:
    language_counter.update(row['LanguagesWorkedWith'].split(';')) #keeps counting the values 
  #inside csv file and related to the 'LanguagesWorkedWith' key. 
##Another way of doing the above using pandas:
    
data = pd.read_csv('data.csv')  
id = data['Responder_id'] 
lang_responses = data['LanguagesWorkedWith'] 
for response in lang_responses:
    language_counter.update(response.split(';'))
    
print(language_counter) #prints out the counter values in a form of a dictionary.
print(language_counter.most_common(15))  #using the 'most_common' method to print the 15 most 
#common languages worked with; in the form of a list, in which each item is a tuple containing the langauge and the count.

##Now let's plot them. First we need to create lists with languages and their count:
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0]) #assigns the first value of each tuple to languages
    popularity.append(item[1])#assigns the second value of each tuple to popularity  

print(languages)    
print(popularity) 
#Now that we have the lists, let's plot them:
plt.bar(languages, popularity)
    
plt.xlabel('Programming Languages')
plt.ylabel('Number of People Who Use')
plt.title('Most Popular Languages')


languages.reverse() 
popularity.reverse() #reverses the items in the list. Did this to change the order of the bar chart to ascending.
plt.barh(languages, popularity)   #when having many items, horizontal bar chart may be more readable.
plt.xlabel('Number of People Who Use')
plt.ylabel('Programming Languages')
plt.title('Most Popular Languages')



##plt.legend(['All Devs', 'Python']) #adds legend to the plot using a list. First item 
#in the list refers to the first plot line, and second to the second line.
#another way to add legends is adding labels to the plt.plot and just use plt.legend()
plt.legend()
plt.tight_layout()

##PIE CHART

slices = [60,40, 15, 10] #create a list as the source for the pie chart. It doesn't have to ad up to 100, bcuz pie chart will deal with that if it doesn't add up to 100.
labels = ['Sixty', 'Forty', 'Fifteen', 'Ten']
colors = ['blue', 'red', 'yellow', 'green']
#Hex colors:
    #Blue: #008fd5
    #Red: #fc4f30
    #Yellow: #e5ae37
    #Green: #6d904f
colours = ['#008fd5','#fc4f30','#e5ae37', '#6d904f'] #using Hex colors instead.
plt.pie(slices, labels = labels, colors = colours, wedgeprops={'edgecolor': 'black'}) #pie chart command

slices = [5833, 7201, 7331, 7920, 18017, 18523, 20524, 23030, 27097, 31991, 35917, 36443, 47544, 55466, 59219]
labels = ['Assembly', 'Go', 'Ruby', 'Other(s):', 'C', 'TypeScript', 'C++', 'PHP', 'C#', 'Bash/Shell/PowerShell', 'Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})
#too many items for a pie chart. Let's just try it for 5 items in the list.
slices5 = [35917, 36443, 47544, 55466, 59219]
labels5 = ['Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
explode =[0, 0.1, 0, 0, 0] #to emphasize a certain slice of the pie, explode is used. 
#0.1 means that 10% of the radius would be bumped out of center.
#shadow=True adds a bit of shadow along the edges.
#startangle = 90 means that the first value of the list starts at 90 degrees.
#autopct='%1.1f%%' shows the percentages on each slice.
plt.pie(slices5, labels=labels5, explode = explode, startangle = 90, shadow= True,
        autopct='%1.1f%%',  wedgeprops={'edgecolor': 'black'})
plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.show()

##STACK CHARTS
minutes = [1,2,3,4,5,6,7,8,9]
player1 = [1,2,3,3,4,4,4,4,5] #player's points at that minute.
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,2,2,2,3,3,3]
labels = ['player1', 'player2', 'player3'] 
colors1 = ['#008fd5', '#fc4f30', '#e5ae37']
plt.stackplot(minutes, player1, player2, player3, labels = labels, colors = colors1 )

plt.legend(loc ='upper left') #considering the ascending nature of the grpah, moving the legend to upper left.
plt.legend (loc = (0.07, 0.05)) #using coordinates(7% from left, 5% from the bottom) for legend location.
plt.title('My Awesome Stack Plot')
plt.tight_layout()
plt.show()

#FILLED LINE PLOTS
data1 = pd.read_csv('data_1.csv')
ages = data1['Age']
dev_salaries = data1['All_Devs']
py_salaries = data1['Python']
js_salaries = data1['JavaScript']

plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

plt.plot(ages, py_salaries, label = 'Python')

overall_median = 57287
plt.fill_between(ages, py_salaries, alpha = 0.25) 
#fill the plot below py_salaries line and ages(x axis). alpha determines the see-through level.
plt.fill_between(ages, py_salaries, overall_median, alpha = 0.25) 
#fill area between py_salaries and overall_median.
plt.fill_between(ages, py_salaries, overall_median, where =(py_salaries>overall_median), 
                 interpolate = True, alpha = 0.25) 
#conditional determines which part of the plot to be filled.
#interpolate to make sure all of the areas get filled correctly.
plt.fill_between(ages, py_salaries, overall_median, where =(py_salaries<=overall_median), 
                 interpolate = True, alpha = 0.25)
#conditional defines another area to be filled with a different color bcuz of 2 separate commands.
plt.fill_between(ages, py_salaries, overall_median, where =(py_salaries<=overall_median), 
                 interpolate = True, color ='red', alpha = 0.25)
#same as previous, just using a custom color (red) here.


#Now let's plot py and dev salaries and fill the area between them with different colors and labels.
plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

plt.plot(ages, py_salaries, label = 'Python')
plt.fill_between(ages, py_salaries, dev_salaries, where =(py_salaries>dev_salaries), 
                 interpolate = True, alpha = 0.25, label ='Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, where =(py_salaries<=dev_salaries), 
                 interpolate = True, color ='red', alpha = 0.25, label = 'Below Avg')
 

plt.legend()
plt.title('Median Salary(USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()

##HISTOGRAMS
ages = [18,19,21,25,26,26,30,32,38,45,55]
bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins=5, edgecolor = 'black') #just define the number of bins(5 here). Pyhton will create and divide data to 5 bins automatically.
plt.hist(ages, bins= bins, edgecolor = 'black') #we assign the bins by defining the exact 
#boundaries. So the right edge is 10, first bin is 10-20, and the left edge is 60.

data = pd.read_csv('data.csv')  
id = data['Responder_id']
bins1 = [10,20,30,40,50,60,70,80,90, 100]
plt.hist(ages, bins= bins1, edgecolor = 'black')
plt.hist(ages, bins= bins1, edgecolor = 'black', log=True) #transform to logarithmic scale.
#Let's add a median line to the histogram.
medain_age = 29
color = '#fc4f30'
plt.axvline(medain_age, color = color, label = 'Median Age', linewidth=2)

plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show()

##SCATTER PLOTS
plt.style.use('seaborn')
x = [5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
plt.scatter(x,y, s=100, c = 'green', edgecolors='black', linewidths=1, alpha=0.75) 
#s=number:dot size; c='colors': dot color; edgecolor and linewidth: line around dots; alpha: transparency.
#c can be either a color like black, green, etc. or a list like 'colors' that assigns different
#color values to different dots. cmap can be used to define the color spetrum used.
colors = [7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
#different sizes can be assigned to dots using a list as the input.
plt.scatter(x,y, s= sizes, c = colors, cmap ='Greens', edgecolor='black', linewidths=1, alpha=0.75) 
cbar = plt.colorbar() #creates a sidebar color spectrum
cbar.set_label('Satisfaction') #assigns a label for the sidebar spectrum.

#applying scatter plot to a csv file.
data = pd.read_csv('2019-05-31-data.csv') 
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c= ratio, cmap = 'summer', edgecolor='black', linewidths=1, alpha=0.75) 
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
plt.xscale('log') #applies logarithmic scale to data points in x axis.
plt.yscale('log') #applies logarithmic scale to data points in y axis.

plt.title('Trending Youtube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.show()

#TIME SERIES PLOTTING
from datetime import datetime, timedelta 
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
    ]
y = [0,1,3,4,6,5,7]

plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate() #gcf(get current format)-run auto format method on x_date for better format.
date_format = mpl_dates.DateFormatter('%b, %d %Y') #change date format
plt.gca().xaxis.set_major_formatter(date_format) #set the new date format

#apply to csv file:

data2 = pd.read_csv('data2.csv')
price_date = data2['Date']
price_close = data2['Close']
data2['Date'] = pd.to_datetime(data2['Date']) #change string format to date time format.
data2.sort_values('Date', inplace= True) #sort data frame based on 'Date' PERMANENTLY.

plt.plot_date(price_date, price_close, linestyle='solid')


plt.title('Bitcoin Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()

##PLOT LIVE DATA IN REAL TIME
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')
x_vals1 = [0,1,2,3,4,5]
y_vals1 = [0,1,3,2,3,5]
 
plt.plot(x_vals1, y_vals1) 

index = count() #count function counts one number at a time.
x_vals = []
y_vals = []
#define a function that generates new values and add them to the lists.
def animate(i):
    x_vals.append(next(index)) #append a value that is count up by 1.
    y_vals.append(random.randint(0, 5)) # append a random value between 1 and 5.
    
    plt.cla() #clear the current axis.
    plt.plot(x_vals, y_vals)
    
#want to live-plot the data that is being generated by the above function.
ani = FuncAnimation(plt.gcf(), animate, interval = 1000) #interval =1000 means 1 second interval.

plt.tight_layout()
plt.show()


##SUBPLOT
