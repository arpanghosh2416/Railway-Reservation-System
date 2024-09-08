#IMPORTING PACKAGES 
import streamlit as st
import sqlite3 as sql
import pandas as pd

conn = sql.connect('railway.db')
current_pages = 'Login/SignUp'
c=conn.cursor()

def create_DB_if_not_available():
    #Creating a table for users
    c.execute('''CREATE TABLE IF NOT EXISTS users
              (username TEXT, password TEXT)''')
    #Creating a table for employee
    c.execute('''CREATE TABLE IF NOT EXISTS employee
              (employee_Id TEXT, password TEXT, designation TEXT)''')
    #Create a table for train details
    c.execute('''CREATE TABLE IF NOT EXISTS train
              (train_No TEXT, train_Name TEXT, departure_Date, starting_Date TEXT, ending_Designation TEXT)''')

create_DB_if_not_available()

#function to create the seat table for merging with train database.
def create_Seat_Table(train_No):
    c.execute(f'''
CREATE TABLE IF NOT EXISTS seats_{train_No}(
              seat_Number INTEGER PRIMARY KEY,
              seat_Type TEXT,
              booked INTEGER,
              passenger_Name TEXT,
              passenger_Age INTEGER,
              passenger_gender TEXT
              )
              ''')
    for i in range(1,51):
        val=0 #need to change the value
        c.execute(f'''
                    INSERT  into seats_{train_No}
                    (seat_No, seat_Type, booked, passenger_Name, passenger_Age, passenger_Gender) 
                    VALUES(?,?,?,?,?);''',(i,val,0,"","",""))



def add_Train(train_No, train_Name, departure_Date, starting_Designation, ending_Designation):
    c.execute("INSERT into trains(train_No, train_Name, departure_Date, starting_Designation, ending_Designation) VALUES(?,?,?,?,?)",
              (train_No,train_Name, departure_Date,starting_Designation,ending_Designation))
    conn.commit()
    