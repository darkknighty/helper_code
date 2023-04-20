import sqlite3
from IPython.display import Image
from io import BytesIO

# Connect to SQLite database
conn = sqlite3.connect('your_database_file.db')

# Get image blob using unique ID
cursor = conn.cursor()
cursor.execute("SELECT image_blob FROM your_table WHERE unique_id=?", (your_unique_id,))
image_blob = cursor.fetchone()[0]

# Display image in Jupyter notebook
Image(data=BytesIO(image_blob))