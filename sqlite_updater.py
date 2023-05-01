import os
import sqlite3

# Mapping of column names to file names
image_columns = {'image1': 'image1.jpg', 'image2': 'image2.jpg', 'image3': 'image3.jpg', 'image4': 'image4.jpg', 'image5': 'image5.jpg', 'image6': 'image6.jpg', 'image7': 'image7.jpg', 'image8': 'image8.jpg'}

# Connect to SQLite database
conn = sqlite3.connect('my_db.sqlite')
c = conn.cursor()

# Loop through files in directory and update table
for filename in os.listdir('image_directory'):
    if filename.endswith('.jpg'):
        # Get column name corresponding to file name
        column_name = image_columns[filename[:-4]]
        
        # Open image file as binary and read content
        with open(os.path.join('image_directory', filename), 'rb') as f:
            image_data = f.read()
        
        # Update table with image BLOB
        c.execute('UPDATE my_table SET {}=? WHERE id=?'.format(column_name), (image_data, 1)) # Replace "1" with appropriate ID value

# Commit changes and close connection
conn.commit()
conn.close()
