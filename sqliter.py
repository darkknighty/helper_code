import sqlite3
import os

# Path to the folder containing the db files
folder_path = "/path/to/folder"

# Connect to the SQLite database and select the attribTable
def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT uniqueid, matrix, frame1_x, frame2_x, frame3_x FROM attribTable")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Iterate through the files in the folder and extract data from the database tables
def extract_data():
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".db"):
            file_path = os.path.join(folder_path, file_name)
            rows = connect_db(file_path)
            data += rows
    return data

# Call the extract_data() function to retrieve the data from the database tables
data = extract_data()

# Print the retrieved data
for row in data:
    print(row)
