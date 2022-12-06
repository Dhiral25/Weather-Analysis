import csv
import pandas as pd
import os
import mysql.connector
import wget



DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE Boston_Weather_Nov22 (Date_Nov INT ,Max_Temperature INT,"
                " Avg_Temperature VARCHAR(25) PRIMARY KEY,Min_Temperature INT,"
              "Max_Dew_Point INT, Avg_Dew_Point INT,Min_Dew_Point INT,"
               "Max_Humidity INT, Avg_Humidity INt, Min_Humidity INT,"
                "Max_Wind_Speed INT, Avg_Wind_Speed INT,Min_Wind_Speed INT,"
                "Max_Pressure INT, Avg_Pressure INT, Min_Pressure INT,Total_Precipitation INT)")

df = pd.read_csv(r'C:\Users\Asus\Desktop\BostonWeatherNov22.csv')
print(df)

# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.Boston_weather_Nov22 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()

DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE Boston_form_response (city VARCHAR(255), Avg_Temperature VARCHAR(25),FOREIGN KEY(Avg_Temperature) REFERENCES Boston_Weather_Nov22(Avg_Temperature), public_opinion VARCHAR(255), clothing VARCHAR(255), frequency_illness VARCHAR(255), heater_req VARCHAR(255), gas_electricity_usage VARCHAR(255))")

df = pd.read_csv(r'C:\Users\Asus\Desktop\DmddAss3\Boston_form_response.csv')
print(df)
# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.Boston_form_response values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()


DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE NewYork_Weather_Nov22 (Date_Nov INT ,Max_Temperature INT,"
                " Avg_Temperature VARCHAR(25) PRIMARY KEY,Min_Temperature INT,"
              "Max_Dew_Point INT, Avg_Dew_Point INT,Min_Dew_Point INT,"
               "Max_Humidity INT, Avg_Humidity INt, Min_Humidity INT,"
                "Max_Wind_Speed INT, Avg_Wind_Speed INT,Min_Wind_Speed INT,"
                "Max_Pressure INT, Avg_Pressure INT, Min_Pressure INT,Total_Precipitation INT)")

df = pd.read_csv(r'C:\Users\Asus\Desktop\NewYork_Weather_Nov22.csv')
print(df)
# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.NewYork_Weather_Nov22 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()

DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE NewYork_form_response (city VARCHAR(255), Avg_Temperature VARCHAR(25),FOREIGN KEY(Avg_Temperature) REFERENCES NewYork_Weather_Nov22(Avg_Temperature), public_opinion VARCHAR(255), clothing VARCHAR(255), frequency_illness VARCHAR(255), heater_req VARCHAR(255), gas_electricity_usage VARCHAR(255))")


df = pd.read_csv(r'C:\Users\Asus\Desktop\DmddAss3\NewYork_form_response.csv')
print(df)
# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.NewYork_form_response values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()


DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE Colorado_Weather_Nov22 (id INT,Date_Nov VARCHAR(25),Avg_Temperature VARCHAR(25) PRIMARY KEY,"
                " Avg_Humidity INT,Avg_Dew_Point INT,"
              "Avg_barometer INT, Avg_Wind_Speed INT,Avg_Gust_Speed INT,"
               "Avg_Direction INT, Rain_For_Month INT, Rain_For_Year INT,"
                "Max_Rain_Per_Min INT, Max_Temperature INT,Min_Temperature INT,"
                "Max_Humidity INT, Min_Humidity INT, Max_Pressure INT,Min_Pressure INT, Max_Wind_Speed INT, Max_Gust_Speed INT,Max_Heat_Index INT)")

df = pd.read_csv(r'C:\Users\Asus\PycharmProjects\pythonProject5\Colorado_Weather_Nov22.csv')
print(df)
# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.Colorado_Weather_Nov22 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()


DmddAss2= mysql.connector.connect(host='localhost', user='root', passwd='root@123', database='testing')
mycursor = DmddAss2.cursor()
#Creating Tables for MySQL Workbench
mycursor.execute("CREATE TABLE Colorado_form_response (city VARCHAR(255), Avg_Temperature VARCHAR(25),FOREIGN KEY(Avg_Temperature) REFERENCES Colorado_Weather_Nov22(Avg_Temperature), public_opinion VARCHAR(255), clothing VARCHAR(255), frequency_illness VARCHAR(255), heater_req VARCHAR(255), gas_electricity_usage VARCHAR(255))")


df = pd.read_csv(r'C:\Users\Asus\Desktop\DmddAss3\Colorado_form_response.csv')
print(df)
# Inserting Data into MySQL WOrkbench
for i,row in df.iterrows():
    sql = "INSERT INTO testing.Colorado_form_response values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    DmddAss2.commit()







