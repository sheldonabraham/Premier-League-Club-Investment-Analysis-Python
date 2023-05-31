#!/usr/bin/env python
# coding: utf-8

# ### Domain: Sports
# ### Context:
# The investment firm, which has a good reputation, typically invests in high-quality sports teams that show promise. They have a dataset that contains important information about all the clubs that have taken part in the premier league, including data on the number of goals they have scored, the number of times they have finished in the top two positions, and other pertinent details.
# ### Data:
# PL Final Data.csv - The dataset includes information on all the clubs that have participated in the premier league tournaments to date.
# ### Data Dictionary:
# *   Club: The name of the football club
# *   Matches: The number of matches the club has played in the Premier League
# *   Wins: The number of matches won by the club in the Premier League
# *   Loss: The number of matches lost by the club in the Premier League
# *   Draws: The number of matches drawn by the club in the Premier League
# *   Clean Sheets: The number of matches in which the club has prevented the opposing side from scoring
# *   Team Launch: The year in which the club was founded
# *   Winners: The number of times the club has won the Premier League
# *   Runners-up: The number of times the club has finished as runners-up in the Premier League
# *   lastplayed\_pl: The year in which the team last played in the Premier League
# ### Project Objecive:
# The firm's management is looking to invest in a top-performing club in the English Premier League, but some of the more established clubs have already been acquired by competitors. To help with the decision-making process, the analytics department has been asked to create a detailed report on the performance of various clubs. The firm is looking to identify clubs that they can approach and potentially invest in to ensure a successful and profitable deal.
# ###### Note: 
# The dataset has been downloaded from the internet using multiple sources. All the credit for the dataset goes to the original creator of the data
# ### Key learning after this project:
# * Data cleaning refers to the process of detecting and correcting errors, inconsistencies, and inaccuracies in a dataset to ensure that it is accurate and reliable.
# 
# * Observation writing involves examining the data and taking note of any significant findings, anomalies, or areas of interest that may arise during the analysis.
# 
# * Exploratory Data Analysis (EDA) is the process of analyzing and visualizing a dataset to understand its main characteristics, such as the distribution of data, the relationships between variables, and any patterns or anomalies that may exist. The primary objective of EDA is to uncover insights and trends that can inform further analysis or decision-making. It is typically the first step in any data analysis project, as it provides a foundation for more advanced statistical methods and models.
# 
# * When dealing with null values in a dataset, domain-specific imputation can be used to fill in missing values based on knowledge of the domain or subject matter. This approach can help ensure that the imputed values are accurate and consistent with the underlying data.
# 

# In[1]:


# installing packages and importing libraries for data cleaning and data analysis
import numpy as np
import pandas as pd


# In[2]:


# Get the csv file into Python
df = pd.read_csv(r'C:\Users\sheld\OneDrive\Desktop\proj\PL Club Investment Analysis\PL Final Data.csv')


# In[3]:


df[df['Runners-up']==7]['Club']


# ## 1. Exploring the Dataset
# 

# In[4]:


df[df['Runners-up']==7]['Club']


# In[5]:


# To view the first 5 rows
df.head()


# After reviewing the dataset, we have observed that it contains 11 columns. The first column contains the name of the football club, while the remaining 10 columns provide information on the club's performance in the Premier League. However, we have identified some data quality issues. Specifically, the club column appears to have numerical values attached to it, which may indicate a serial number, and the runners-up column contains null values. We will need to perform further analysis to determine the best approach for handling

# In[6]:


# To view the last 5 rows
df.tail()


# Upon reviewing the dataset, we have identified some data quality issues. Specifically, we have noticed that the TeamLaunch column has inconsistencies, where most clubs have a year mentioned, but one club has a month and year mentioned instead. This inconsistency could potentially cause problems in the analysis, so the column should be cleaned to ensure consistency. Additionally, we have observed null values in the Winners column, which will need to be addressed as part of the data cleaning process.

# In[7]:


# Size of the dataset
df.shape


# There are 40 rows and 11 columns.

# In[9]:


# To get more information about datatypes and null values
df.info()


# After examining the dataset, we have determined that there are no missing values as all columns have 40 non-null values. However, we have previously identified null values in the 'Winners' and 'Runners-up' columns.
# Additionally, we have noticed that the data type for the 'Runners-up' column is non-numeric (i.e., object type). To conduct any numerical analysis on this column, we will need to convert it to a numeric data type.

# ## 2. Cleaning the Dataset

# In[10]:


# Let's start with the Club column

df['Club']= df['Club'].str.replace('\d+', '')

# The regular expression pattern '\d+' used in this code matches one or more digits at the beginning of a string 
# str.replace() replaces this pattern with an empty string,
# effectively removing the numbers from the front of each team name in the "Club" column.


# In[11]:


# Lets's view the data again
df.head()


# We see that the numbers have been removed from the club names under the Club column.

# In[12]:


df["Winners"].isnull()


# In[13]:


# Now, let's examine the "Winners" column using an alternative approach:
df["Winners"].isnull().any()
# In this code, the isnull() method is applied to the "Winners" column of the DataFrame 
# isnull() returns a boolean Series where each element indicates whether the corresponding value in the column is null (True) or not (False)
# The any() method is then used to confirm whether there is at least one True value in the Series, indicating the existence of null values.


# In[14]:


df['Winners'].value_counts() 

# This will return the count of unique values in the "Winners" column and the number of times each value occurs


# After reviewing the dataset, we have found that there are a total of 25 non-null values in the "Winners" column. Additionally, we have observed that none of the 18 football clubs listed has won the Premier League title, as the "Winners" column displays a count of 0 for each club.
# 
# Furthermore, we have analyzed the counts and determined that there have been 30 Premier League tournaments held in the past (1992-2022, one tournament per year). Out of the 25 football clubs with non-zero and non-null values in the "Winners" column, 3 clubs have won the Premier League title once, 1 club has won it thrice, 1 club has won it 5 times, another club has won it 6 times, and 1 club has won it a remarkable 13 times, totaling to 30 victories.
# 
# This indicates that all other clubs in the dataset have not won any Premier League matches. Therefore, to ensure that the dataset accurately reflects the historical performance of each club in terms of Premier League wins, it would be appropriate to replace the null values in the "Winners" column with 0.
# 

# In[15]:


df["Winners"].fillna(0, inplace=True)
# this will replace all null values with "0" in the winners column


# In[16]:


df["Winners"].isnull().any()
# Checking for null values in the "Winners" column 


# In[17]:


# Let's look at the runner-ups
df['Runners-up'].value_counts()


# We see that teams have different number of runner-up finishes. We also notice ann inconsistency, which need to be cleaned.

# In[18]:


# No. of runner-ups
1+1+1+6+4+5+3+7+2


# In[19]:


# Given that we have data for all 30 Premier League tournaments that have been conducted, it is appropriate to update the "Winners" column by replacing any null values and '-' with 0 for all clubs that have not won the Premier League title
# We replace '-' and null values with zero
df['Runners-up'].fillna(0, inplace=True)
df['Runners-up'].replace('-', 0, inplace=True)


# In[20]:


# Also we have seen it earlier that 'Runners-up' column is "Object" type let us convert it into int type
df['Runners-up'] = pd.to_numeric(df['Runners-up'], errors='coerce')
df['Runners-up'] = df['Runners-up'].astype('Int64')


# This code aims to change the data type of the "Runners-up" column in a pandas DataFrame named "df" from an "Object" type to an "Int64" type.
# 
# The first line utilizes the pd.to_numeric() function to try to convert the "Runners-up" column into a numeric data type. The errors='coerce' parameter directs the function to replace any values that cannot be converted to a number with NaN.
# 
# The second line applies the .astype() method to the "Runners-up" column of the DataFrame, converting it to an "Int64" data type. The "Int64" argument specifies the desired data type.

# In[21]:


# Checking the datatype
df.info


# In[22]:


# We also notice inconsistency in Teamlaunch column
df['TeamLaunch'].value_counts()


# In[23]:


#  Converting 'TeamLaunch' into 'YYYY' (datetime format)

df['TeamLaunch'] = pd.to_datetime(df['TeamLaunch'], errors='coerce')

# convert the column to YYYY format
df['TeamLaunch'] = df['TeamLaunch'].dt.strftime('%Y')


# The first line of code converts the column 'column_name' to datetime format using the pandas to_datetime() function. The 'errors' parameter is set to 'coerce', which means that any invalid dates will be set to NaT (Not a Time) in the resulting datetime column.
# 
# The second line of code uses the dt.strftime() method to convert the datetime column to a string column with only the year values. '%Y' is the format code for the year. This line of code will create a new column 'column_name' in the format YYYY.

# In[24]:


df['TeamLaunch'].value_counts()


# In[25]:


df.dtypes['lastplayed_pl']


# In[26]:


df['lastplayed_pl'] = (pd.to_datetime(df['lastplayed_pl'], format='%b-%y', errors='coerce')).dt.year

#The "format" parameter specifies the expected format of the input string. 
#In this case '%b-%y' indicates a three-letter month abbreviation followed by a two-digit year (e.g. "Mar-21")


# In[27]:


df['lastplayed_pl']


# ## 3. Data Analysis

# In[28]:


df.describe()


# Each team in the competition played an average of 573.75 games, and they collectively scored an average of 769 goals. The median amount of goals scored is 462, which is much less than the average and shows that some clubs have scored significantly more goals than others.
# 
# It's interesting to note that the median number of victories and runners-up finishes are both 0, indicating that the majority of teams have not triumphed or placed second in the competition. But one team has won the competition an incredible 13 times, and another has finished second seven times. What teams these are would be interesting to learn.

# In[29]:


df[df['Winners']==13]['Club']
# Which team won the league 13 times


# In[30]:


# Team that has been runner-up 7 times
df[df['Runners-up']==7]['Club']


# We see that Manchester United has won Premier league 13 times and have been runner-up 7 times.

# In[31]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[32]:


# Let's visulalise the match played column, creating a histogram
plt.hist(df['Matches Played'])

# adding labels and title
plt.xlabel('No. of Matches Played')
plt.ylabel('Frequency')
plt.title('Histogram of Matches Played')


# The histogram reveals that the majority of teams have played fewer than 400 games. However, a few teams have played more than 900 games, which is an extraordinarily high quantity.
# 
# It is important to note that several of the most prestigious clubs have previously been owned by rivals, in accordance with the project's requirements. The client is therefore interested in finding potential clubs that, despite their lack of Premier League experience, may do well in the future.

# In[34]:


# Let's see which teams have played more than 900 games.
df[df['Matches Played']>=900]['Club']


# Analysis led us to the conclusion that 11 clubs in total have a disproportionately higher level of Premier League experience than the other clubs. These teams have a greater amount of games under their belts and have shown to be seasoned pros in the league.
# 
# We are looking for potential clubs that, despite their lack of Premier League experience, may succeed in the future in order to meet the needs of the customer. Since their established status in the league may distort our results and make it challenging to discover less experienced clubs with great potential, we have decided to remove these 11 clubs from our research.
# 
# By removing these clubs, we can focus our analysis on the remaining clubs and potentially identify hidden gems that may have been overlooked due to their lack of experience in the league.

# In[35]:


df[df['Matches Played'] < 900]
# teams that have played less than 900 games


# In[36]:


df = df[df['Matches Played'] < 900].reset_index(drop=True)


# In[37]:


df.head()


# In[39]:


df.shape


# It is important to realise that the figures in each column correspond to the total points earned across all of the games.
# 
# We must normalise the statistics by dividing the number of wins, losses, draws, clean sheets, and goals by the total number of matches played in order to properly assess the performance of the teams.
# 
# We will have a good notion of each team's winning, losing, draw, and clean sheet percentages as well as their goals per game.

# In[41]:


# Create new columns for Winning Rate, Loss Rate, Draw Rate, & Clean Sheet Rate
df['Winning Rate'] = (df['Win'] / df['Matches Played'])*100
df['Loss Rate'] = (df['Loss'] / df['Matches Played'])*100
df['Drawn Rate'] = (df['Drawn'] / df['Matches Played'])*100
df['Clean Sheet Rate'] = (df['Clean Sheets'] / df['Matches Played'])*100


# In[42]:


# Creating a column for average goals scored per match

df['Avg Goals Per Match']=df['Goals']/df['Matches Played']

df['Avg Goals Per Match']=df['Avg Goals Per Match'].round()


# In[43]:


df.head()


# The columns have succesfully been added.

# In[44]:


# Now let us visualize Winning, Loss, Drawn rate, and Clean Sheet

# Set the figure size
plt.figure(figsize=(8, 6))

# Create the boxplot
boxplot = plt.boxplot([df['Winning Rate'], df['Drawn Rate'], df['Loss Rate'], df['Clean Sheet Rate']], 
                      patch_artist=True,
                      labels=['Winning Rate', 'Drawn Rate', 'Loss Rate', 'Clean Sheet Rate'])

# Set the title and axis labels
plt.title('Distribution of Winning Rate, Drawn Rate, Loss Rate and Clean Sheet Rate')
plt.xlabel('Winning, Drawn ,Lost Game & Clean Sheet')
plt.ylabel('Rate')

# Show the plot
plt.show()


# ### Winning Rate
# We notice that the Winning Rate boxplot contains a few outliers that are above the upper whisker. It is safe to say that these outlier clubs have outperformed the other clubs in terms of winning percentages. Let's start by identifying them.
# 
# Let's also determine which club has the lowest "Winning Rate"
# 
# ### Drawn Rate
# We notice an anomaly in the drew rate boxplot, showing that one club has a significantly greater drawn rate than the rest. This may not always be a good sign because it signifies that the team may find it difficult to win games. Let's find out which club this is before going any farther.
# 
# ### Loss Rate
# We see that these clubs have higher loss rates than victory rates.
# 
# ### Clean Sheet Rate
# We see that data for Clean Sheet Rate is pretty symmetric

# In[45]:


# Identify clubs with high winning rate

# Calculate the interquartile range for the "Winning Rate" column
Q1 = df['Winning Rate'].quantile(0.25)
Q3 = df['Winning Rate'].quantile(0.75)
IQR = Q3 - Q1

# Calculating the upper boundaries for potential outliers <-- Expectional high winning rate compared to other teams
upper_bound = Q3 + 1.5 * IQR

# Clubs with high winning rate 
highwinningrate = df[(df['Winning Rate'] > upper_bound)]
highwinningrate


# We have found out that Blackburn Rovers and Leeds United have high winning rates of 37.6% and 38.8% respectively.

# In[46]:


# Now for low winning rate

# Calculate the lower boundaries for potential outliers <-- Low winning rate compared to other teams
lower_bound = Q1 - 1.5 * IQR

# Clubs with lowest winning rate 
lowwinningrate = df[(df['Winning Rate'] < lower_bound)]
lowwinningrate


# Hull City has the lowest winning rate of 21.5%

# In[47]:


# Now for drawn rate
# Calculate the interquartile range for the "Drawn Rate" column
Q1 = df['Drawn Rate'].quantile(0.25)
Q3 = df['Drawn Rate'].quantile(0.75)
IQR = Q3 - Q1

# Calculate the upper boundaries for potential outliers <-- Expectional high winning rate compared to other teams
upper_bound = Q3 + 1.5 * IQR

highwinningrate = df[(df['Drawn Rate'] > upper_bound)]
highwinningrate


# Brighton & Hove Albion is expectionally high Drawn Rate at 33%

# In[48]:


# Let's see the 'Avg Goals Per Match' column

df['Avg Goals Per Match'].describe()


# In[49]:


# Let's see the 'Winners' and 'Runners-up' columns

df['Winners'].value_counts()


# In[50]:


df['Runners-up'].value_counts()


# We observe that out of the 29 clubs, only 2 clubs have won the Premier League, and one club has been a runner-up. Let us identify these clubs

# In[51]:


df[(df['Winners']==1) | (df['Runners-up']==1)]


# We see that Blackburn Rovers have won Premier League and also been Runners-ups once each whereas Leicester City has won Premier League once.

# In[52]:


# Lets us again analyse Matches Played Column for our reduced dataframe (29 clubs).

df['Matches Played'].describe()


# In[53]:


# Let's look at the "lastplayed_pl" column

df['lastplayed_pl'].value_counts()


# Only 8 out of the 29 clubs are currently playing in the premier league. We will give teams that have played more recently more weight when reaching the final selection and give teams that haven't played recently less weight.

# In[54]:


# The 8 clubs that are currently playing

df[df['lastplayed_pl']==2023]['Club']


# It is desirable to give Premier League teams with more recent experience a higher priority.

# ## 4. Final Recommendations Framework
# Let's create a plan to Score each team on the pre defined metric.
# 
# * Give a score of 10 if club have a relatively high experience in the Premier League above average (372)
# * Give a score of 15 if club has winning rate above Q3
# * Give a score of 15 if club has lossing rate below Q1
# * Give a score of 10 if club drawn rate below Q1 and losing rate is below Q1
# * Give a score of 10 if club has clean sheet above Q3 and winning rate is above Q3
# * Give a score of 15 if club has won premier league
# * Give a score of 10 if club has been a runners-up in premier league
# * Give a score of 15 if club has been currently playing in premier league

# In[55]:


# Calculate the upper bound for the "Winning Rate" column
upper_bound_WinningRate = df['Winning Rate'].quantile(0.75)

# Calculate the lower bound for the "Loss Rate" column
lower_bound_LosingRate = df['Loss Rate'].quantile(0.25)

# Calculate the lower bound for the "Drawn Rate" column
lower_bound_DrawnRate = df['Drawn Rate'].quantile(0.25)

# Calculate the upper bound for the "Drawn Rate" column
upper_bound_CleanSheetRate = df['Clean Sheet Rate'].quantile(0.75)


# In[56]:


len(df)


# In[57]:


df['scores']=np.zeros(len(df))


# In[58]:


df.head()


# In[59]:


df.loc[df['Matches Played'] >= 372, 'scores'] += 10
df.loc[df['Winning Rate'] >= upper_bound_WinningRate, 'scores'] += 15
df.loc[df['Loss Rate'] <= lower_bound_LosingRate, 'scores'] += 15
df.loc[(df['Drawn Rate'] <= lower_bound_DrawnRate) & (df['Loss Rate'] <= lower_bound_LosingRate), 'scores'] += 10
df.loc[(df['Clean Sheet Rate'] >= upper_bound_CleanSheetRate) & (df['Winning Rate'] >= upper_bound_WinningRate), 'scores'] += 10
df.loc[df['Winners'] == 1, 'scores'] += 15
df.loc[df['Runners-up'] == 1, 'scores'] += 10
df.loc[df['lastplayed_pl'] == 2023, 'scores'] += 15


# In[60]:


# sort the DataFrame by score in descending order
df_sort = df.sort_values(by='scores', ascending=False)

# create a bar chart of team scores
plt.figure(figsize=(25,10))
plt.bar(df_sort['Club'], df_sort['scores'], color='blue')

# add labels and title to the chart
plt.ylabel('Scores', fontsize=16)
plt.title('Football Club v/s performance score', fontsize=18)

# add legend to explain the blue bars
plt.legend(['Scores'], fontsize=14)

# rotate the team names on the x-axis for readability
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)

# set the y-axis limit to start from 0 and end at 100
plt.ylim(0, 100)

# display the chart
plt.show()


# A deeper look at the list reveals that Blackburn Rovers, the team we currently lead, is absent. Investigate further and learn the most recent season Blackburn Rovers competed in order to better grasp their performance. Our analysis will benefit greatly from having this context, which will also help us appropriately judge their current performance.

# In[61]:


df[df['Club']=='Blackburn Rovers']['lastplayed_pl']


# The last time Blackburn Rovers participated in the competition was in 2012, which was a long time ago. With this knowledge, we advise stakeholders to think about funding Leicester City instead. We think Leicester City is a better investment because to their recent success and form.
# 
# We will do extra secondary research to substantiate our assertion and offer more proof of Leicester City's present performance and success potential.
# 
# According to our research, Blackburn Rovers were relegated to the Championship league in 2012 i.e., league below Premier League and later to League One in 2017 i.e., league below Championship league. However, they were promoted back to the Championship in 2018 and have since finished in the middle of the table in recent years. Given their inconsistent performance and lack of presence in the Premier League since 2012, it would be inappropriate to recommend this club for investment.
# 
# On the other hand, Leicester City, the 2016 Premier League champions, have consistently finished in the top 10 in recent years. They placed 5th in both the 2019-2020 and 2020-2021 seasons and finished 8th in 2021-2022. With sufficient financial backing, Leicester City has the potential to achieve even greater success in the near future. Therefore, it would be reasonable to recommend Leicester City to our clients.
# 
# Source 1: https://www.transfermarkt.co.in/blackburn-rovers/platzierungen/verein/164
# 
# Source 2: https://www.transfermarkt.co.in/leicester-city/platzierungen/verein/1003
# 
# ## We recommend investing in Leicester City based on our analysis

# In[ ]:




