#Pandas

#to import pandas (pd is the common shorthand for pandas methods)

import pandas as pd 

#limit the number of rows that pandas will display when we ask for data frames to be
#displayed

pd.options.display.max_rows = 20

#read in some data and assign it to a variable

nfl_data = pd.read_csv('2015_stats.csv')

#inspect the data

nfl_data.head()
nfl_data.tail()
nfl_data.sample() #a random selection of rows. this one can be slow for large files

nfl_data.head(3) #only shows the first three rows

#lets say that the first row is wrong, and we only want from row 2 onwards...

nfl_data = nfl_data[1:] #note the index for row 2 is 1 (because row 1 is 0)

#now lets say that I want some general info about the dataframe - such as the
#data type in each column and whehter there are NAs

nfl_data.info()


#if some of the numeric data is inappropriately labelled as a string, we can
#convert it to numeric like this. (using data in the Passing Attempts column)

nfl_data['Passing Attempts'] = pd.to_numeric(nfl_data['Passing Attempts'])


'''
Lets say that your column headers include some preceding whitespace. These can be
removed like this:
(note the python style short-hand for loop)
'''

nfl_data.columns = [column_name.strip(' ') for column_name in nfl_data.columns]


#the data also has this weird feature where all the columns with home team stats 
#end with .1  - it would make more sense to replace the .1 with H, which is more 
#intuitive

nfl_data.columns = [x.replace('.1', '_H') for x in nfl_data.columns]

#now we have the _H suffix, it would be good to have corresponding _V suffixes
#for the visiting team. So let's find the columns without _H (and a few exceptions)
#and add _V suffix to them.

nfl_data.columns = [x + '_V' 
                    if x.find('_H')==-1 and x not in ['Date', 'Vis Team', 'Home Team'] 
                    else x
                    for x in nfl_data.columns]

#We've cleaned the data up a bit now, so let's export it back to a CSV
#let's not include an additional column that adds the column index

nfl_data.to_csv('cleaned_nfl_data.csv',index=False)


#to convert a string/numbers to a date:

nfl_data['Date'] = pd.to_datetime(nfl_data['Date'])

#quickly get summary statistics for each column

nfl_data.describe()


#how do you get all of the unique values within a column?

set(nfl_data['Home Team']) #this will also arrange them alphabetically, the output is a column vector in braces.
nfl_data['Home Team'].unique() #this will not arrange them alphabetically, the output is also a row vector array

#how many of them are there?

len(set(nfl_data['Home Team']))


#alternatively, you can do the last two steps in one with:

nfl_data['Home Team'].nunique()



#Now lets say that I want to know how each team did in each column, using some summary
#statistic, such as sum.
#For this you use group_by()

nfl_data.groupby('Home Team').sum()


#You can also use the apply function to do multiple actions across the dataframe:

#The Home Team column contains leading white blank spaces. Can you use the apply() function to get rid of them? 
nfl_data['Home Team'] = nfl_data['Home Team'].apply(lambda x: x.strip(' '))

#How would you return the number of passing completions for the first home game 
#played by each team? You may want to use sort_values()  to make sure that your 
#data is chronologically ordered.
nfl_data.groupby('Home Team').apply(lambda x: x.sort_values(['Date'])['Passing Completions_H'].head(1))



'''
The above was from the built in sherlock tutorials

the following is from the getting started ML tutorial using the meteor data set
'''

#To sort rows acording to some criteria (this will show all columns however, but only the first 5 rows)

df.sort_values(['mass_g'], ascending=[False])[0:5] 


#if you want to access a particular row, using it's index (iloc in newer versions of pandas):

df.sort(['mass_g'], ascending=[False]).iloc[:, 2]



#------------------------
#ASI Fellowship specific tutorial

#Series
#A series is a 1D array of indexed data.
#You can think of it as like a dataframe with one row,
#Or alternatively think of a dataframe like a series with multiple rows
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])

#the series object has a few built in methods associated with it
#if you just want to kno the values:
data.values

#if you want to know the indexes:
#indexes are like the column headers or the key's from a dictionary
data.index

#To get to a data point using a position index

data.iloc[1] #this would return 0.5, i.e. the 2nd number in the series

data.iloc[1:3] #this returns 0.5 and 0.75, i.e. the 2nd and 3rd (but not 4th) elements and their index values

#You can also get to the data using the index value
data.loc['b'] #returns 0.5
data.loc['b':'c'] #returns 0.5 and 0.75, so here the thing after the colon is included

#Convert a dictionary to a series
population = pd.Series(population_dict)




#DataFrames
#DF's are another fundamental building block of pandas

#create a dataframe
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)


#add the population series from before (a few lines above)
states = pd.DataFrame({'population': population,
                       'area': area})

#get info on the series
states.index #this would give the row names, which in this case is the names of the states

#get the titles of the columns
states.columns


#get the area's column
states['area']

#create a third column that calculates pop density from the other two, and call it density
states['density'] = states['population'] / states['area']
states



#Missing Data
#pandas/numpy use NaN to represent missing data
#missing data is written as:

np.nan
None

#example of a series with a NaN/None
data = pd.Series([1, np.nan, 'hello', None])

#check if a series has a nan
data.isnull()

#get all the values from a series that are null
data.dropna()

#note that the series you create will maintain their original index values
#which if numeric, may mean that numbers are missing

#convert NaN's to 0
data.fillna(0)



#Concatenation and merging

#vertical concatenation, note the explicit indexing, because we know that we'll
#later be concatenating.
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)



#Aggregate functions and grouping
df.mean()

#with optional axis specification
df.sum(axis='columns')

#several common aggregates: count, mean, std, min, max, quartiles
df.describe()


#grouping by a certain value within a column is a bit funny
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])

df.groupby('key')
#this will find the unique values within key, i.e. A, B and C 
#but it won't actually produce a table with them, it's just some
#object pointing to where the relevant data is.
#You then apply an aggregate function to this object like this:

df.groupby('key').sum()



#String operations

data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
names = pd.Series(data)

#Convert all charaters to capitals
names.str.capitalize()




#Reading in data and inspecting/manipulating it

df = pd.read_csv('data/meteors.csv', encoding="ISO-8859-1")
df.head(2)
df.describe()
df[7:10] #show the 7th, 8th, 9th rows
df.loc[:5, 'place'] #show the first 5 rows of place column
df.loc[-3:, :5] #last 3 rows of the first 5 columns
df[['mass_g','year']].head() #only get the first few rows of the mass and year columns

#compute a histogram of the counts and the first 10 rows
df['type_of_meteorite'].value_counts()[:10]

#Can also use dot notation to index columns, but beware...
#if the column name matches a method or contains numbers it may get weird
df.fell_found.value_counts()[:5]


#A few ways of finding specific rows based on the data of one column
is_after_1999 = df['year'] > 1999 # boolean mask
since_1999 = df[is_after_1999] # select based on values

is_l6 = df['type_of_meteorite'] == "L6" 
df[is_after_1999 & is_l6].head(2)




#Chaining commands (and plots, requires matplotlib)

# create a bar plot
(df.loc[(df['year'] > 1999), 'year'].astype(int)
                                    .value_counts()
                                    .sort_index()
                                    .plot('bar'));

#create a scatter plot
(df.loc[(df['year']>1950), ('mass_g','year')].plot(kind='scatter', x='year',y='mass_g'))
