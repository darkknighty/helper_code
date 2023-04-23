import sqlite3
import os

# Path to the folder containing the db file
folder_path = "/path/to/folder"

# Connect to the SQLite database and select the newTable
def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT uniqueid, img1_matrix, img2_matrix, img3_matrix FROM newTable")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Compare the matrices of the images in each row to find matching images
def find_matching_images():
    data = connect_db(os.path.join(folder_path, "database.db"))
    matching_images = []
    for row1 in data:
        for row2 in data:
            if row1 != row2: # skip self-comparison
                for i in range(1, 4):
                    for j in range(1, 4):
                        if row1[i] == row2[j]:
                            match = (row1[0], i, row2[0], j) # uniqueids and indices of the two matching images
                            matching_images.extend(match) # append the match tuple to the results list
    return matching_images

# Call the find_matching_images() function to retrieve the matching images
matching_images = find_matching_images()

# Print the matching images
for i in range(0, len(matching_images), 4):
    print(f"Matching images: {matching_images[i:i+4]}")
