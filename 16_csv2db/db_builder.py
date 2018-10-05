# Daniel Keriazis and Karen Li
# SoftDev1 pd7
# SQLITE3 BASICS
# 2018-10-04

import sqlite3  # Enable control of an sqlite database
import csv  # Facilitates CSV I/O

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE)  # Open if file exists, otherwise create
c = db.cursor()  # Facilitate db ops

def insert(table, values):
    # Build SQL stmt, save as string
    command = 'INSERT INTO ' + table + ' VALUES '
    command += str(values)
    c.execute(command)  # Run SQL statement

# Create table courses
c.execute("CREATE TABLE courses (code TEXT, mark INT, id INT)")
# Create table peeps
c.execute("CREATE TABLE peeps (name TEXT, age INT, id INT)")

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        insert('courses', (row['code'], int(row['mark']), int(row['id'])))

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        insert('peeps', (row['name'], int(row['age']), int(row['id'])))

db.commit()  # Save changes
db.close()  # Close database

