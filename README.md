# Video Game Sales Analysis

# Short Description
This project involves analyzing video game sales data using Python (Pandas) and MySQL. The primary goal is to identify the number of games launched between 2000 and 2005. Additional analysis includes running simple and complex SQL queries and filtering data using Python.

# Getting Started

## Prerequisites
- Python 3.x
- Pandas library
- MySQL server
- SQLAlchemy library
- PyMySQL library


## Installing
### 1. Clone the repository:
https://github.com/zeel94/Assignment---5.git

### 2. Install required Python libraries:
pip install pandas sqlalchemy pymysql

### 3. Set up MySQL:
Install MySQL server.
Create a database and import the vgsales table.

# Running the Tests

## Breakdown of Tests
### Part 1: Data Import and Filtering
Read CSV files into DataFrames:
```python
import pandas as pd
df_test = pd.read_csv(r'D:\DC Study\Data-1202\vgsales.csv')
Filter games launched between 2000 and 2005:
between_00_05 = df_test[(df_test["Year"] >= 2000) & (df_test["Year"] <= 2005)]
print(between_00_05)
```
### Part 2: Simple Queries in MySQL
Set up SQLAlchemy engine and run a simple query:
```python
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://user10:pw@localhost/ap')
conn = engine.connect()
df = pd.read_sql_query("SELECT * FROM data1202.vgsales", conn)
```
### Part 3: Complex Queries in MySQL
Run a complex query to analyze sales:
```python 
complex_df = pd.read_sql_query('''SELECT
    Round(SUM(NA_Sales)) as 'NA_Sales',
    ROUND(SUM(EU_Sales)) as 'EU_Sales',
    ROUND(SUM(JP_Sales)) as 'JP_Sales',
    ROUND(SUM(Global_Sales)) AS 'Global_Sales',
    ROUND((SUM(NA_Sales)/SUM(Global_Sales)) * 100) as 'NA_GlobalShare'
    FROM data1202.vgsales
    WHERE Genre = 'Action' AND Year>= 2005''', conn)
complex_df.head()
```
### Part 4: Filtering Data in Python
Filter DataFrame for Nintendo games:
```python
nintendo_games = df[df['Publisher'] == 'Nintendo']
print("The number of Nintendo games is: " + str(len(nintendo_games)))
Filter action games launched after 2005:
action_05 = df[(df['Genre']=='Action') & (df['Year'] >= 2005)]
print("The max sales of action games in EU after 2005 is: " + str(action_05.EU_Sales.max()))
```
# Deployment
This project does not include deployment steps as it is designed for local analysis and testing.

# Author
Zeel Kayasth
GitHub: zeel94

# License
This project is licensed under the MIT License.

# Acknowledgement
- Thanks to Durham College for the guidance and resources provided.
- Special thanks to the open-source community for the libraries and tools used in this project.
