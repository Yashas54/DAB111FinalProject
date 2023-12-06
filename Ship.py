import sqlite3
import pandas as pd
import csv
import numpy as np
import uuid
from flask import Flask
import pathlib



path = pathlib.Path().cwd()

def create_db(db_name , filename , table_name):
    
    file_path = path/ filename
    
    con = sqlite3.connect('Titanic.db')
    cursor = con.cursor()
    
    Name = pd.read_csv('Titanic Disaster Dataset.csv') 
    Name.to_sql(table_name , con , index = False, if_exists="replace")
    
    result = cursor.execute("SELECT * FROM Name").fetchall()
    print(result)

    con.commit()
    con.close()
    

if __name__=="__main__":
    db_name = "Titanic.db"
    filename = "Titanic Disaster Dataset.csv"
    table_name = "Name"
    create_db(db_name, filename, table_name)