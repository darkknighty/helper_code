import sqlite3
import csv

# connect to the SQLite database
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# get the unique IDs from the SQLite table
c.execute('SELECT DISTINCT id FROM my_table')
sqlite_ids = [row[0] for row in c.fetchall()]

# open the CSV file and add the SQLite IDs as a new column
with open('my_data.csv', 'r') as f:
    reader = csv.reader(f)
    rows = [row + [''] for row in reader]  # add an empty column to each row

with open('my_data_with_ids.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i, row in enumerate(rows):
        if i == 0:  # header row
            writer.writerow(row + ['sqlite_id'])
        else:
            writer.writerow(row + [sqlite_ids[i-1]])
