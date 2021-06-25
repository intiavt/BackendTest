# This script extracts the information present in the API of FUT21 and saves name, position, nation, and club of the player into a local database.

import requests
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="backendtest"
)
mycursor = mydb.cursor()
response = requests.get(
    'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1')

sql = "INSERT INTO players (name, position, nation, club) VALUES (%s, %s, %s, %s)"

for data in response.json()['items']:
    val = (data["name"], data["position"], data["nation"]["name"], data["club"]["name"])
    mycursor.execute(sql, val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)