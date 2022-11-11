import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing Dataset
file = pd.read_csv("Economy_Indicators.csv")
file.head()
# Checking Datatypes of all columns
file.info()
# selcting some countries in country coloum
Country = file.loc[file['Country'].isin(["United Kingdom", "Germany","Italy","France"])]
#Date = file.loc[file['Country'].isin(["United Kingdom"]
# Date = file[file["Country"]=="United Kingdom"]
Country

GDP = Country['GDP']
GDP

Inflation_Rate = Country['Inflation Rate']
Inflation_Rate

Jobless_Rate = Country['Jobless Rate']
Jobless_Rate

country  = Country.loc[:,"Country"]
country

#start Plotting
# Multiple Projections  

fig, ax1 = plt.subplots()
ax1.set_ylabel('GDP ')
ax1.plot(country, GDP , color='green',label='Inflation Rate')
#ax1.set_ylim(0,4000000)
ax1.grid()

ax2 = ax1.twinx()  # join a second axis with the first graph we just made
ax2.set_ylabel(' Inflation Rate')
# # ax2.set_ylim(0,3000000)
ax2.plot(country,Inflation_Rate , color='red',label='GDP')

ax3 = ax1.twinx()  # join a second axis with the first graph we just made
ax3.set_ylabel('Jobless Rate')
# # ax2.set_ylim(0,3000000)
ax3.plot(country, Jobless_Rate, color='blue',label='Jobless Rate')
ax1.legend((), loc='upper right', shadow=True)
# ax1.legend(shadow=True, fancybox=True)
# plt.figure(figsize=(10,4)) 
plt.title("comparison  Inlation , GDP and Joblessrate ")
# plt.legend()
fig.legend()
plt.show()

# Defining Function for Top Ten Graph (Bar Chart)


def topten_barchart(x, y, color, x_label, y_label, title):
    plt.barh(x, y, color=color)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
# Assigning values for GDP to variables for the function
x  = file.nlargest(10, "GDP")["Country"]
y = file["GDP"].nlargest(10)
color = "maroon"
x_label = "GDP"
y_label = "Country"
title = "Top Countries by GDP"

# Using Function
topten_barchart(x, y, color, x_label, y_label, title)
# Assigning values for Unemployment to variables for the function

x = file.nlargest(10, "Jobless Rate")["Country"]
y = file["Jobless Rate"].nlargest(10)
color = "blue"
x_label = "Unemployment"
y_label = "Country"
title = "Top Countries by Unemployment"

# Using Function
topten_barchart(x, y, color, x_label, y_label, title)

# Top 15 Countries by Population (Pie Chart)

x = file["Population"].nlargest(10)
y = file.nlargest(10, "Population")["Country"]

plt.pie(x, labels=y , autopct='%1.0f%%')
plt.show()
