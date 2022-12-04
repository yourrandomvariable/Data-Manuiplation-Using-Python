#!/usr/bin/env python
# coding: utf-8

# # Basic Exercises on Data Importing - Understanding - Manipulating - Analysis - Visualization

# ## Section-1: The pupose of the below exercises (1-7) is to create dictionary and convert into dataframes, how to diplay etc...
# ## The below exercises required to create data 

# ### 1. Import the necessary libraries (pandas, numpy, datetime, re etc)
import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import re

# set the graphs to show in the jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# set seabor graphs to a better style
sns.set(style="ticks")

# ### 2. Run the below line of code to create a dictionary and this will be used for below exercises
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }

# ### 3. Assign it to a object called pokemon and it should be a pandas DataFrame
pokemon = pd.DataFrame(raw_data)
print(type(pokemon))
pokemon.head(1)

# ### 4. If the DataFrame columns are in alphabetical order, change the order of the columns as name, type, hp, evolution, pokedex
re_order = ['name', 'type', 'hp', 'evolution', 'pokedex']
pokemon.loc[:,re_order]

# ### 5. Add another column called place, and insert places (lakes, parks, hills, forest etc) of your choice.
pokemon['place'] = ['lakes', 'parks', 'hills', 'forest']
pokemon.head(1)

# ### 6. Display the data type of each column
pokemon.dtypes

# ### 7. Display the info of dataframe
pokemon.info()

# ## Section-2: The pupose of the below exercise (8-20) is to understand deleting data with pandas.
# ## The below exercises required to use wine.data

# ### 8. Import the dataset *wine.txt* from the folder and assign it to a object called wine
# Please note that the original data text file doesn't contain any header.
# Please ensure that when you import the data, you should use a suitable argument so as to avoid data getting imported as header.
wine = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\wine.csv',header= None)
wine.head(3)

# ### 9. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine.drop(columns= [0,3,6,8,10,12,13],inplace= True)
wine
# ### 10. Assign the columns as below:
# The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 
wine.columns = ['alcohol','malic_acid','alcalinity_of_ash','magnesium','flavanoids','proanthocyanins','hue']
wine.head(1)

# ### 11. Set the values of the first 3 values from alcohol column as NaN
wine.loc[0:3,'alcohol'] = 'NaN'
wine.head(3)

# ### 12. Now set the value of the rows 3 and 4 of magnesium as NaN
wine.loc[3:4,'magnesium'] = 'NaN'
wine.head(5)

# ### 13. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine[wine.alcohol == 'NaN'] = 10
wine.head(5)
wine[wine.magnesium == 'NaN'] = 100
wine.head(5)

# ### 14. Count the number of missing values in all columns.
wine.isnull().sum()

# ### 15.  Create an array of 10 random numbers up until 10 and save it.
random_arr = np.random.randint(low = 0, high = 10, size = 10)
random_arr

# ### 16.  Set the rows corresponding to the random numbers to NaN in the column *alcohol*
wine[wine.loc[:,'alcohol']== 'NaN'] = random_arr

# ### 17.  How many missing values do we have now?
wine.isnull().sum()

# ### 18. Print only the non-null values in alcohol
wine.alcohol.notnull()

### 19. Delete the rows that contain missing values



wine.dropna(inplace = True)

# ### 20.  Reset the index, so it starts with 0 again
wine.reset_index(inplace = True)
wine

# ## Section-3: The pupose of the below exercise (21-27) is to understand ***filtering & sorting*** data from dataframe.
# ## The below exercises required to use chipotle.tsv

# This time we are going to pull data directly from the internet.  
# Import the dataset directly from this link (https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv) and create dataframe called chipo
chipo = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\chipotle.tsv',sep='\t')
chipo.head(3)

# ### 21. How many products cost more than $10.00? 
# 
# Use `str` attribute to remove the $ sign and convert the column to proper numeric type data before filtering.
# 
chipo['item_price'] = chipo['item_price'].str.replace('$', '')
chipo['item_price'] = chipo['item_price'].astype(float)
np.count_nonzero(chipo.item_price > 10.00)

# ### 22. Print the Chipo Dataframe & info about data frame
print(chipo)
chipo.info()

# ### 23. What is the price of each item? 
# - Delete the duplicates in item_name and quantity
# - Print a data frame with only two columns `item_name` and `item_price`
# - Sort the values from the most to less expensive books?
chipo.drop_duplicates(subset = ['item_name','quantity'],inplace = True)
chipo.loc[:,['item_name','item_price']]
chipo.sort_values('item_price',ascending= False)

# ### 24. Sort by the name of the item
chipo.sort_values('item_name',ascending= True)

# print
# ### 25. What was the quantity of the most expensive item ordered?
chipo[chipo.loc[:,'item_price'] == chipo.item_price.max()].quantity

# ### 26. How many times were a Veggie Salad Bowl ordered?
(chipo.item_name == 'Veggie Salad Bowl').sum()

# ### 27. How many times people orderd more than one Canned Soda?
((chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)).sum()
# ## Section-4: The purpose of the below exercises is to understand how to perform aggregations of data frame
# ## The below exercises (28-33) required to use occupation.csv

# ###  28. Import the dataset occupation.csv and assign object as users
users = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\occupation.csv',sep = '|')
users.head(3)

# ### 29. Discover what is the mean age per occupation
users.groupby('occupation').age.mean()

# ### 30. Discover the Male ratio per occupation and sort it from the most to the least.
# 
# Use numpy.where() to encode gender column.
users_male = users[users.loc[:,'gender'] == 'M']
occupation_male = users_male.groupby('occupation').gender.count()
overall_occupation = users.groupby('occupation').gender.count()
calc = (occupation_male/overall_occupation)
calc

# ### 31. For each occupation, calculate the minimum and maximum ages
users.pivot_table('age',index='occupation',aggfunc={'min','max'})

# ### 32. For each combination of occupation and gender, calculate the mean age
users.groupby(['occupation','gender']).age.mean()

# ### 33.  For each occupation present the percentage of women and men
calc * 100
print("Percentage of Men are: ", calc)
print("Percentage of Women are: ",(100 - calc))


# ## Section-6: The purpose of the below exercises is to understand how to use lambda-apply-functions
# ## The below exercises (34-41) required to use student-mat.csv and student-por.csv files 

# ### 34. Import the datasets *student-mat* and *student-por* and append them and assigned object as df
mat = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\student-mat.csv')
por = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\student-por.csv')
mat.head(2)
por.head(2)

# ### 35. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
mat.iloc[:,0:12]
por.iloc[:,0:12]

# ### 36. Create a lambda function that captalize strings (example: if we give at_home as input function and should give At_home as output.
cap = lambda x : x.str.capitalize()

# ### 37. Capitalize both Mjob and Fjob variables using above lamdba function
mother_job = mat['Mjob']
father_job = mat['Fjob']
m_job = por['Fjob']
f_job = por['Mjob']
print("Job's of Father are: ",cap(father_job))
print("Job's of Mother are: ",cap(mother_job))
print("Job's of Father are: ",cap(f_job))
print("Job's of Mother are: ",cap(m_job))

# ### 38. Print the last elements of the data set. (Last few records)
mat.iloc[:,-1].head(5)
por.iloc[:,-1].head(5)

# ### 39. Did you notice the original dataframe is still lowercase? Why is that? Fix it and captalize Mjob and Fjob.
mat.loc[:,['Mjob','Fjob']]= mat.loc[:,['Mjob','Fjob']].apply(cap)
por.loc[:,['Mjob','Fjob']]= por.loc[:,['Mjob','Fjob']].apply(cap)

# ### 40. Create a function called majority that return a boolean value to a new column called legal_drinker
initial_arr = [True, False]
arr = np.random.choice(initial_arr, size=mat.school.count())
bool_arr = pd.DataFrame(list(map(bool, arr)))
majority = lambda x:bool_arr
mat['legal_drinker'] = majority(f_job)
initial_arr = [True, False]
arr = np.random.choice(initial_arr, size=por.school.count())
bool_arr = pd.DataFrame(list(map(bool, arr)))
majority = lambda x:bool_arr
por['legal_drinker'] = majority(f_job)
por
    
# ### 41. Multiply every number of the dataset by 10. 
(mat.select_dtypes(include='int64'))*10
(por.select_dtypes(include='int64'))*10

# ## Section-6: The purpose of the below exercises is to understand how to perform simple joins
# ## The below exercises (42-48) required to use cars1.csv and cars2.csv files 

# ### 42. Import the datasets cars1.csv and cars2.csv and assign names as cars1 and cars2
cars1  = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\cars1.csv')
cars2  = pd.read_csv('C:\\Users\\mriga\\OneDrive\\Desktop\\Multiple Data Sets\\85 Exercise\\cars2.csv')

#    ### 43. Print the information to cars1 by applying below functions 
#    hint: Use different functions/methods like type(), head(), tail(), columns(), info(), dtypes(), index(), shape(), count(), size(), ndim(), axes(), describe(), memory_usage(), sort_values(), value_counts()
#    Also create profile report using pandas_profiling.Profile_Report
profile = ProfileReport(cars1,explorative= True)
profile.to_file('eda_output.html')

# ### 44. It seems our first dataset has some unnamed blank columns, fix cars1
cars1.dropna(axis=1,inplace=True)
cars1.head(3)

# ### 45. What is the number of observations in each dataset?
cars1.shape
cars2.shape

# ### 46. Join cars1 and cars2 into a single DataFrame called cars







# ### 47. There is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
owners = np.random.randint(15000,73000,size = cars1.shape[0])
owners2 = np.random.randint(15000,73000,size = cars2.shape[0])

# ### 48. Add the column owners to cars
cars1['owners'] = owners
cars2['owners'] = owners2

# ## Section-7: The purpose of the below exercises is to understand how to perform date time operations

# ### 49. Write a Python script to display the
# - a. Current date and time
# - b. Current year
# - c. Month of year
# - d. Week number of the year
# - e. Weekday of the week
# - f. Day of year
# - g. Day of the month
# - h. Day of week







# ### 50. Write a Python program to convert a string to datetime.
# Sample String : Jul 1 2014 2:43PM 
# 
# Expected Output : 2014-07-01 14:43:00







# ### 51. Write a Python program to subtract five days from current date.
# 
# Current Date : 2015-06-22
# 
# 5 days before Current Date : 2015-06-17







# ### 52. Write a Python program to convert unix timestamp string to readable date.
# 
# Sample Unix timestamp string : 1284105682
#     
# Expected Output : 2010-09-10 13:31:22







# ### 53. Convert the below Series to pandas datetime : 
# 
# DoB = pd.Series(["07Sep59","01Jan55","15Dec47","11Jul42"])
# 
# Make sure that the year is 19XX not 20XX







# ### 54. Write a Python program to get days between two dates. 







# ### 55. Convert the below date to datetime and then change its display format using the .dt module
# 
# Date = "15Dec1989"
# 
# Result : "Friday, 15 Dec 98"

# ## The below exercises (56-66) required to use wind.data file 

# ### About wind.data:
# 
# The data have been modified to contain some missing values, identified by NaN.  
# 
# 1. The data in 'wind.data' has the following format:
"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""
The first three columns are year, month and day.  The remaining 12 columns are average windspeeds in knots at 12 locations in Ireland on that day. 
# ### 56. Import the dataset wind.data and assign it to a variable called data and replace the first 3 columns by a proper date time index







# ### 57. Year 2061 is seemingly imporoper. Convert every year which are < 70 to 19XX instead of 20XX.







# ### 58. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].







# ### 59. Compute how many values are missing for each location over the entire record.  
# #### They should be ignored in all calculations below. 







# ### 60. Compute how many non-missing values there are in total.







# ### 61. Calculate the mean windspeeds over all the locations and all the times.
# #### A single number for the entire dataset.







# ### 62. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
# 
# #### A different set of numbers for each location.







# ### 63. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# 
# #### A different set of numbers for each day.







# ### 64. Find the average windspeed in January for each location.  
# #### Treat January 1961 and January 1962 both as January.







# ### 65. Calculate the mean windspeed for each month in the dataset.  
# #### Treat January 1961 and January 1962 as *different* months.
# #### (hint: first find a  way to create an identifier unique for each month.)







# ### 66. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.







# ## The below exercises (67-70) required to use appl_1980_2014.csv  file







# ### 67. Import the file appl_1980_2014.csv and assign it to a variable called 'apple'







# ### 68.  Check out the type of the columns







# ### 69. Transform the Date column as a datetime type







# ### 70.  Set the date as the index







# ### 71.  Is there any duplicate dates?







# ### 72.  The index is from the most recent date. Sort the data so that the first entry is the oldest date.







# ### 73. Get the last business day of each month







# ### 74.  What is the difference in days between the first day and the oldest







# ### 75.  How many months in the data we have?







# ## Section-8: The purpose of the below exercises is to understand how to create basic graphs

# ### 76. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches







# ## The below exercises (77-80) required to use Online_Retail.csv file

# ### 77. Import the dataset from this Online_Retail.csv and assign it to a variable called online_rt







# ### 78. Create a barchart with the 10 countries that have the most 'Quantity' ordered except UK







# ### 79.  Exclude negative Quatity entries







# ### 80. Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries
# Hint: First we need to find top-3 countries based on revenue, then create scater plot between Quantity and Unitprice for each country separately
# 







# ## The below exercises (81-90) required to use FMCG_Company_Data_2019.csv file

# ### 81. Import the dataset FMCG_Company_Data_2019.csv and assign it to a variable called company_data







# ### 82. Create line chart for Total Revenue of all months with following properties
# - X label name = Month
# - Y label name = Total Revenue







# ### 83. Create line chart for Total Units of all months with following properties
# - X label name = Month
# - Y label name = Total Units
# - Line Style dotted and Line-color should be red
# - Show legend at the lower right location.

# ### 84. Read all product sales data (Facecream, FaceWash, Toothpaste, Soap, Shampo, Moisturizer) and show it  using a multiline plot
# - Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).







# ### 85. Create Bar Chart for soap of all months and Save the chart in folder







# ### 86. Create Stacked Bar Chart for Soap, Shampo, ToothPaste for each month
# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

# ### 87. Create Histogram for Total Revenue







# ### 88. Calculate total sales data (quantity) for 2019 for each product and show it using a Pie chart. Understand percentage contribution from each product







# ### 89. Create line plots for Soap & Facewash of all months in a single plot using Subplot







# ### 90. Create Box Plot for Total Profit variable






