#!/usr/bin/env python
# coding: utf-8

# # Video Game Sales Analysis Project
# ## Project Overview
# 
# In this project, you'll analyze video game sales data to identify patterns that determine a game's success. Working as an analyst for the online store Ice, you'll use this information to help plan future advertising campaigns.
# 
# ## Environment Setup and Required Libraries

# In[1]:


# Import all required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


# ## Step 1: Loading and Initial Data Exploration
# 
# First, let's load our dataset and examine its basic properties:

# In[2]:


# Load the dataset
df = pd.read_csv('/datasets/games.csv')


# In[3]:


# Display basic information about the dataset
display(df)
display(df[df['Name']== 'Grand Theft Auto V'])


# In[4]:


# Check for duplicate entries
print(df.duplicated().sum())


# ### Key Questions to Answer:
# - What's the total number of records in our dataset?
# - What data types are present in each column?
# - Are there any obvious issues with the data?
# - Do we see any immediate patterns or anomalies?

# ## Step 2: Data Preparation
# 
# ### 2.1 Standardizing Column Names

# In[5]:


# Convert column names to lowercase
df.columns = df.columns.str.lower()


# In[6]:


# Verify the changes
print(df.columns)


# ### 2.2 Data Type Conversion

# In[7]:


# Check current data types
df.info()


# In[8]:


# Make changes to data types if necessary
# Describe the columns where the data types have been changed and why.

#'user_score' is a numeric values and should be convert to 'float' instead set as 'object'
df['user_score'] = df['user_score'].replace('tbd', np.nan).astype(float) 

#Year is whole-number values so should be convert into 'int' instead of 'float'
#datatype set to 'int64' for flexibly when dealing with missing values
df['year_of_release'] = df['year_of_release'].astype('Int64') 


# In[9]:


# Pay attention to the abbreviation TBD (to be determined). Specify how you intend to handle such cases.

#TBD values are treated as missing, so I replaced them with NaN to allow numerical operations and future imputation


# ### 2.3 Handling Missing Values

# In[10]:


# Examine missing values
df.isna().sum()


# In[11]:


# Calculate percentage of missing values
percent_missing = df.isnull().sum() * 100 / len(df)
print(round(percent_missing,2))


# In[12]:


# Analyze patterns in missing values

# For 'percent_missing' < 5% -> use imputation to replace missing values 
# For 'percent_missing' > 30% -> using placeholder as NAN 


# In[13]:


# Handle missing values based on analysis
# Your code here to handle missing values according to your strategy

#leave missing values as NaN for this analysis


# In[14]:


# Why do you think the values are missing? Give possible reasons.
# Answer: avoid filling missing values to avoid distorting analysis patterns and maintain data credibility


# <b> Student's comment:</b>
# thank you for reviewing and give me helpful feedback :)
# 

# ### 2.4 Calculate Total Sales

# In[15]:


# Calculate total sales across all regions and put them in a different column
#displaying how much sale for each game
df['total_sale'] = df['na_sales']+df['eu_sales']+df['jp_sales']+df['other_sales']
display(df)


# # Step 3: Analyzing Video Game Sales Data
# 
# ## 3.1 Temporal Analysis of Game Releases
# Let's first examine the distribution of game releases across different years to understand our data's coverage and significance:

# In[16]:


# Create a DataFrame with game releases by year
game_by_year = df.groupby('year_of_release')


# In[17]:


#Calculate Distribute of game each year
game_by_year = game_by_year.size()

game_by_year = game_by_year.reset_index()

game_by_year.columns = ['year_of_release', 'number_of_games']


# In[18]:


# Display summary statistics for each year
#display(game_per_year)
game_by_year.plot( x = 'year_of_release', y = 'number_of_games', 
                   title = 'Game Distribution per Year',
                   xlabel = 'year', ylabel = 'numbers of games', legend = False )
plt.show()


# ### Questions to Consider:
# - Which years show significant numbers of game releases?
# - Are there any notable trends or patterns in the number of releases?
# - Is there enough recent data to make predictions for 2017?

# ## 3.2 Platform Sales Analysis Over Time
# 
# Now let's analyze how sales vary across platforms and years:

# In[19]:


# Calculate total sales by platform and year
sale_per_genre = df.groupby(['year_of_release', 'genre'])

sale_per_genre = sale_per_genre['total_sale'].sum()
display(sale_per_genre)


# In[20]:


# Create a heatmap of platform sales over time
heatmap_data = sale_per_genre.unstack(fill_value=0)

plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu')
plt.title('Total Sales by Year and Genre')
plt.ylabel('Year of Release')
plt.xlabel('Genre')
plt.show()


# In[21]:


# Identify platforms with declining sales
sale_per_genre = sale_per_genre.reset_index()

plt.figure(figsize=(12,6))

for genre, group in sale_per_genre.groupby('genre'):
    # sort by year to keep lines smooth
    group = group.sort_values('year_of_release')
    plt.plot(group['year_of_release'], group['total_sale'], label=genre)

plt.title("Total Sales Over Time by Genre")
plt.xlabel("Year of Release")
plt.ylabel("Total Sales")
plt.legend()
plt.show()


# ### Questions to Consider:
# - Which platforms show consistent sales over time?
# - Can you identify platforms that have disappeared from the market?
# - What's the typical lifecycle of a gaming platform?

# ## 3.3 Determining Relevant Time Period
# 
# Based on your analysis above, determine the appropriate time period for predicting 2017 sales:

# In[22]:


# Your code here to filter the dataset to relevant years
# Example:
relevant_years = [2013,2014,2015,2016] # Replace with your chosen years
df_relevant = df[df['year_of_release'].isin(relevant_years)]
# Justify your choice with data
#The 5 years timeframe captures recent market trends, platforms, and consumer behavior.
display(df_relevant)


# ### Document Your Decision:
# - What years did you select and why?
# - How does this period reflect current market conditions?
# - What factors influenced your decision?

# ## 3.4 Platform Performance Analysis
# 
# Using your selected time period, let's analyze platform performance:

# In[23]:


# Analyze platform sales trends
platform_sales = df_relevant.groupby('platform')['total_sale'].sum().reset_index()
display(platform_sales)


# In[24]:


# Sort platforms by total sales
platform_sales = platform_sales.sort_values('total_sale',ascending=False)
display(platform_sales)


# In[25]:


# Visualize top platforms
(platform_sales.head(5)).plot(x = 'platform', y = 'total_sale', 
                              kind ='bar', title = 'Top platforms sales from 2012-2016',
                             xlabel = 'platform names', ylabel = 'total sales', legend = False)

# Calculate year-over-year growth for each platform
sales_by_year_platform = df_relevant.groupby(['year_of_release', 'platform'])['total_sale'].sum().reset_index()
sales_pivot = sales_by_year_platform.pivot(index='year_of_release', columns='platform', values='total_sale')

# Your code here to calculate and visualize platform growth rates
growth = sales_pivot.pct_change()
print(growth)


# ## 3.5 Sales Distribution Analysis
# 
# Let's examine the distribution of sales across platforms:

# In[26]:


# Create box plot of sales by platform
plt.figure(figsize=(12,6))
sns.boxplot(x='platform', y='total_sale', data= sales_by_year_platform)
plt.title("Distribution of Game Sales by Platform")
plt.show()


# In[27]:


# Calculate detailed statistics for each platform
stats_by_platform = sales_by_year_platform.groupby('platform')['total_sale'].agg(
    count='count',
    mean='mean',
    median='median',
    min='min',
    max='max',
    std='std').reset_index()

print(stats_by_platform)


# ## 3.6 Review Score Impact Analysis
# 
# Select a popular platform and analyze how reviews affect sales:

# In[28]:


# Choose a popular platform based on your previous analysis
popular_platform = df[df['platform'].isin(['3DS','PS3','PS4','X360','XOne'])]
display(popular_platform)


# In[29]:


# Create scatter plots for both critic and user scores


# In[30]:


# Critic Scores
sns.stripplot(x='platform', y='critic_score', data=popular_platform, jitter=True, alpha=0.6)
plt.title("Critic Scores Across Platforms")
plt.show()

# User Scores
sns.stripplot(x='platform', y='user_score', data=popular_platform, jitter=True, alpha=0.6)
plt.title("Critic Scores Across Platforms")
plt.show()

# Calculate correlations
print(popular_platform[['critic_score', 'user_score']].corr())


# ## 3.7 Cross-Platform Comparison
# 
# Compare sales performance of games across different platforms:

# In[31]:


# Find games released on multiple platforms
dup_games = (df[df['name'].duplicated()]) 
display(dup_games)


# In[32]:


# Compare sales across platforms for these games
# Your code here to analyze and visualize cross-platform performance
(df[df['name'] == 'Grand Theft Auto V']).plot(x = 'platform', y = 'total_sale', 
                                              kind = 'bar', legend = False,
                                              ylabel = 'total sales (in million)', title = 'Grand Theft Auto V Total Sales Across Platforms')


# ## 3.8 Genre Analysis
# 
# Finally, let's examine the distribution of games by genre:

# In[33]:


# Analyze genre performance
sale_per_genre =  df.groupby('genre')['total_sale'].sum().reset_index()
display(sale_per_genre)


# In[34]:


# Sort genres by total sales
sale_per_genre = sale_per_genre.sort_values(by='total_sale', ascending=False)
display(sale_per_genre)


# In[35]:


# Visualize genre distribution
sale_per_genre.plot(x = 'genre', y = 'total_sale',kind = 'bar', ylabel = 'total sales (in million)', 
                    title = 'Total Sales across Game Genres', legend = False)


# In[36]:


# Calculate market share for each genre
market_share = df.groupby('genre')['total_sale'].sum()
market_share = (market_share / market_share.sum()) * 100
display(market_share)


# ### Key Questions for Genre Analysis:
# - Which genres consistently perform well?
# - Are there any genres showing recent growth or decline?
# - How does the average performance vary across genres?

# # Step 4: Regional Market Analysis and User Profiles
# 
# In this section, we will analyze the gaming market characteristics across three major regions: North America (NA), Europe (EU), and Japan (JP). Our analysis will focus on platform preferences, genre popularity, and the impact of ESRB ratings in each region.
# 
# ## 4.1 Regional Platform Analysis
# 
# Let's begin by examining platform performance across different regions:

# In[37]:


# Function to analyze platform performance by region
def analyze_platform_performance(data):
    regions = ['na_sales', 'eu_sales', 'jp_sales']
    platform_performance = df.groupby('platform')[regions].sum()
    return platform_performance


# In[38]:


# Analyze each region
platform_performance = analyze_platform_performance(df)
display(platform_performance)


# ### Cross-Regional Platform Comparison
# 
# Let's create a comparative analysis of platform performance across regions:

# In[39]:


# Create a comparative platform analysis
def get_top_platforms_by_region(data, region, top_n=5):
    return df.sort_values(by=region, ascending=False).head(top_n)

# Example for North America
top_platforms = get_top_platforms_by_region(platform_performance, 'na_sales')
display(top_platforms)


# In[40]:


# Visualize cross-regional comparison for top platforms
top_platforms.plot(x = 'platform', y = 'na_sales', kind = 'bar')


# ## 4.2 Regional Genre Analysis
# 
# Now let's examine genre preferences across regions:

# In[41]:


# Function to analyze genre performance by region
def analyze_genre_performance(data):
    regions = ['na_sales', 'eu_sales', 'jp_sales']
    genre_performance = data.groupby('genre')[regions].sum()
    return genre_performance
genre_performance = analyze_genre_performance(df)
display(genre_performance)


# ### Cross-Regional Genre Comparison
# 
# Let's compare genre preferences across regions:

# In[42]:


# Create a comparative genre analysis
genre_market_share = genre_performance.div(genre_performance.sum())
display(genre_market_share)

genre_market_share.plot(kind='bar', figsize=(10,6))
plt.title('Genre Market Share by Region')
plt.ylabel('Market Share')
plt.xlabel('Genre')
plt.show()


# ## 4.3 ESRB Rating Impact Analysis
# 
# Finally, let's examine how ESRB ratings affect sales in each region:

# In[43]:


# Function to analyze ESRB rating impact
def analyze_esrb_impact(data):
    regions = ['na_sales', 'eu_sales', 'jp_sales']
    esrb_performance = data.groupby('rating')[regions].sum()
    return esrb_performance
    
esrb_performance = analyze_esrb_impact(df)
display(esrb_performance)


# In[44]:


# Analyze ESRB impact for each region
esrb_market_share = esrb_performance.div(esrb_performance.sum())
display(esrb_market_share)


# # Step 5 : Hypothesis Tests
# 
# —Average user ratings of the Xbox One and PC platforms are the same.
# 
# —Average user ratings for the Action and Sports genres are different.
# 
# Set the *alpha* threshold value yourself.
# 
# Explain:
# 
# —How you formulated the null and alternative hypotheses
# 
# —What criteria you used to test the hypotheses~~,~~ and why
# 

# In[45]:


# Filter the data
xbox_ratings = df[df['platform'] == 'XOne']['user_score'].dropna()
pc_ratings = df[df['platform'] == 'PC']['user_score'].dropna()

action_ratings = df[df['genre'] == 'Action']['user_score'].dropna()
sports_ratings = df[df['genre'] == 'Sports']['user_score'].dropna()

# Perform t-tests
alpha = 0.05

t_stat1, p_val1 = ttest_ind(xbox_ratings, pc_ratings, equal_var=False)
t_stat2, p_val2 = ttest_ind(action_ratings, sports_ratings, equal_var=False)

print("Xbox vs PC p-value:", p_val1)
print("Action vs Sports p-value:", p_val2)

# Interpret results
if p_val1 < alpha:
    print("Reject H0: Significant difference in average user ratings between Xbox One and PC.")
else:
    print("Fail to reject H0: No significant difference between Xbox One and PC.")

if p_val2 < alpha:
    print("Reject H0: Significant difference in average user ratings between Action and Sports genres.")
else:
    print("Fail to reject H0: No significant difference between Action and Sports genres.")


# # Step 6. Write a general conclusion
# 

# From this analysis, I see that Action and Sports games dominate global sales, while Japan strongly prefers Role-Playing games.
# Platforms like PlayStation and Xbox drive the largest sales, with big variability in performance across titles.
# 
# Sales peaked around 2008–2010 and have declined since, showing clear market cycles. Regionally, preferences differ: NA and EU lean toward Action and Shooter games, Japan toward Role-Playing.
# 
# Hypothesis tests showed no major difference in user ratings between Xbox One and PC, but there is a difference between Action and Sports genres, suggesting genre impacts user satisfaction more than platform.
# 
