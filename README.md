# Video Game Sales Analysis (Ice Online Store)

## Project Overview
This project analyzes historical video game sales data to identify patterns that determine whether a game is commercially successful. The analysis is conducted from the perspective of **Ice**, an online video game retailer, with the goal of identifying potential best-selling games and informing advertising campaign strategies.

The dataset includes global sales figures, platform information, genres, user and critic reviews, and ESRB ratings. Using data available up to **2016**, the analysis simulates planning a marketing campaign for **2017**.

---

## Objectives
- Identify trends in video game releases and sales over time  
- Compare performance across gaming platforms  
- Analyze how reviews and genres influence sales  
- Build regional user profiles (North America, Europe, Japan)  
- Test statistical hypotheses related to user ratings  

---

## Dataset Description
The dataset (`games.csv`) contains the following columns:

- **Name** — Game title  
- **Platform** — Gaming platform (e.g., Xbox One, PlayStation)  
- **Year_of_Release** — Release year  
- **Genre** — Game genre  
- **NA_sales** — North American sales (USD millions)  
- **EU_sales** — European sales (USD millions)  
- **JP_sales** — Japanese sales (USD millions)  
- **Other_sales** — Sales in other regions (USD millions)  
- **Critic_Score** — Professional review score (max 100)  
- **User_Score** — User review score (max 10)  
- **Rating** — ESRB age rating  

> ⚠️ Note: Data for 2016 may be incomplete.

---

## Data Preparation
The following preprocessing steps were performed:
- Standardized column names to lowercase  
- Converted columns to appropriate data types  
- Handled missing values with documented reasoning  
- Processed `"TBD"` values in user scores  
- Created a new column for **total global sales** (sum of all regional sales)  

---

## Exploratory Data Analysis
The analysis includes:
- Number of games released per year  
- Sales trends across platforms and platform life cycles  
- Identification of currently profitable and declining platforms  
- Box plots comparing global sales by platform  
- Correlation analysis between reviews and sales  
- Sales performance comparisons across platforms  
- Genre-based sales distribution and profitability  

---

## Regional User Profiles
For each region (NA, EU, JP), the following were identified:
- Top 5 platforms and market share differences  
- Top 5 genres and regional preferences  
- Impact of ESRB ratings on sales  

---

## Hypothesis Testing
The following hypotheses were tested using statistical methods:
1. The average user ratings of **Xbox One** and **PC** are the same  
2. The average user ratings for **Action** and **Sports** genres are different  

For each hypothesis:
- Null and alternative hypotheses were defined  
- Significance level (alpha) was selected  
- Appropriate statistical tests were applied  
- Results were interpreted and explained  

---

## Tools & Technologies
- Python  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- SciPy  
- Jupyter Notebook  

---

## Project Structure
The analysis is completed in a Jupyter Notebook, with:
- Code in executable cells  
- Explanations and conclusions in Markdown cells  
- Clear formatting and section headings  

---

## Key Takeaways
This project demonstrates practical experience in:
- Data cleaning and preprocessing  
- Exploratory data analysis  
- Statistical hypothesis testing  
- Data visualization  
- Drawing business-oriented conclusions from data  

---

## Author
Hillary

