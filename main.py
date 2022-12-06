import bs4
from bs4 import BeautifulSoup
import csv
import requests
import time
import pandas as pd
import urllib
import re
import pickle
import os
import mysql.connector
import wget

from datetime import datetime

# COllecting Data by Web Scraping

Dates_r = pd.date_range(start='11/1/2022', end='11/30/2022', freq='D')
dates = [str(i)[:4] + str(i)[5:7] for i in Dates_r]
dates[0:5]

df_list = []
index = []
for k in range(len(dates)):
    url = "http://www.estesparkweather.net/archive_reports.php?date="
    url += dates[k]

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('table')
type(table)

raw_data = [row.text.splitlines() for row in table]
raw_data = raw_data[:-9]
raw_data

for i in range(len(raw_data)):
    raw_data[i] = raw_data[i][2:len(raw_data[i]):3]
raw_data

for u in url:
    for i in range(len(raw_data)):
        c = ['.'.join(re.findall("\d+", str(raw_data[i][j].split()[:5]))) for j in range(len(raw_data[i]))]

        df_list.append(c)
        index.append(dates[k] + c[0])
    f_index = [index[i] for i in range(len(index)) if len(index[i]) > 6]
    data = [df_list[i][1:] for i in range(len(df_list)) if len(df_list[i][1:]) == 19]

from datetime import datetime

final_index = [datetime.strptime(str(f_index[i]), '%Y%m%d').strftime('%Y-%m-%d') for i in range(len(f_index))]

# Data Cleaning - Renaming the columns
col = ['Average temperature (°F)', 'Average humidity (%)',
       'Average dewpoint (°F)', 'Average barometer (in)',
       'Average windspeed (mph)', 'Average gustspeed (mph)',
       'Average direction (°deg)', 'Rainfall for month (in)',
       'Rainfall for year (in)', 'Maximum rain per minute',
       'Maximum temperature (°F)', 'Minimum temperature (°F)',
       'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
       'Minimum pressure', 'Maximum windspeed (mph)',
       'Maximum gust speed (mph)', 'Maximum heat index (°F)']
df = pd.DataFrame(data, columns=col, index=final_index)
df.head(30)
df.to_csv('November22_Colorado.csv')

# Data Cleaning - Deleting Multiple Duplicate Rows
df_state = pd.read_csv('November22_Colorado')
Dup_Rows = df_state[df_state.duplicated()]
DF_RM_DUP = df_state.drop_duplicates(keep='first')
print(DF_RM_DUP)
DF_RM_DUP.to_csv('Colorado_Weather_Nov22.csv')

# Data Cleaning - Checking for Null Values (No Null values found in our case)
print(DF_RM_DUP.isnull().sum())




