import os
import pandas as pd
import xml.etree.ElementTree as ET

def process_excel(root_path, excel_path, csv_path):
    # Read the Excel data into a DataFrame
    df = pd.read_excel(excel_path)

    # Create the CSV file if it doesn't exist
    if not os.path.isfile(csv_path):
        with open(csv_path, 'w') as f:
            f.write('Folder Name,File Name,' + ','.join(df.columns[2:]) + '\n')

    # Iterate over the DataFrame rows
    with open(csv_path, 'a') as f:
        for index, row in df.iterrows():
            # Get the first two columns
            folder_name = os.path.join(root_path, row[df.columns[0]], row[df.columns[1]])

            # Create the path to the XML file
            xml_path = os.path.join(folder_name, 'record.xml')

            # Check if the XML file exists
            if not os.path.isfile(xml_path):
                print(f'XML file {xml_path} not found!')
                continue

            # Parse the XML file
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # Find the data corresponding to the XPath column
            xpath = row[df.columns[2]]
            element = root.find(xpath)

            # Check if the element was found
            if element is None:
                print(f'Element {xpath} not found in {xml_path}!')
                continue

            # Write the row data to the CSV file
            csv_row = [folder_name, row[df.columns[1]], element.text] + [str(row[column]) for column in df.columns[3:]]
            f.write(','.join(csv_row) + '\n')
