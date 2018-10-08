import sqlite3  # Enable control of an sqlite database
import csv  # Facilitates CSV I/O

DB_FILE="database.db"

db = sqlite3.connect(DB_FILE)  # Open if file exists, otherwise create
c = db.cursor()  # Facilitate db ops

counts = {}
totals = {}
averages = {}
names = {}

command = "SELECT name,code,mark,courses.id FROM courses,peeps WHERE courses.id = peeps.id"
c.execute(command)

for i in c.fetchall():  # Get output of SELECT statement
    name, code, mark, student = i
    if student not in counts:
        counts[student] = 0
        totals[student] = 0
    counts[student] += 1
    totals[student] += mark
    names[student] = name

# Iteratre through all student ids and add them to the averages dict
for student in counts:
    total = totals[student]
    count = counts[student]
    averages[student] = round(total / count, 1)  # Calculate average
    print(names[student], student, averages[student])

# Create table peeps_avg with unique ids corresponding to student averages
c.execute("CREATE TABLE peeps_avg (id INT PRIMARY KEY, avg INT)")

# Add rows to peeps_avg with id and avg
for student in averages:
    c.execute("INSERT INTO peeps_avg VALUES ({id}, {avg})"  # Add new row
            .format(id=student, avg=averages[student]))  # Use proper values

db.commit()  # Save changes
db.close()  # Close database

