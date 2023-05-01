import os
import csv
import xml.etree.ElementTree as ET

# Set the directory path where the XML files are located
dir_path = 'path/to/folder'

# Define the fields to extract from the XML file
fields = ['name', 'age', 'address']

# Create the CSV file and write the header row
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id'] + fields)
    writer.writeheader()

    # Loop through each folder in the directory
    for folder in os.listdir(dir_path):
        folder_path = os.path.join(dir_path, folder)

        # Loop through each file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.xml'):
                file_path = os.path.join(folder_path, filename)

                # Parse the XML file and extract the data
                tree = ET.parse(file_path)
                root = tree.getroot()
                row = {'id': folder}
                for field in fields:
                    row[field] = root.find(field).text

                # Write the row to the CSV file
                writer.writerow(row)
