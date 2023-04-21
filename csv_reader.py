import pandas as pd
import os

# read the CSV file into a pandas dataframe
df = pd.read_csv('data.csv')

def get_csv_data(file_name):

    # extract the first two columns
    col1 = df.iloc[:, 0]
    col2 = df.iloc[:, 1]
    col3 = df.iloc[:, 5]

    # create a list of tuples with the three columns
    data = list(zip(col1, col2, col3))

    # create a path string for each tuple
    paths = [os.path.join(t[0], t[1], str(t[2])) for t in data]

    # print the resulting paths
    return paths, df    

data, df = get_csv_data(file_name)

# set the path suffix for the XML files

def extract_records(data):
    # iterate over the data tuples
    new_cols = []  # create an empty list to hold the new column values

    for item in data:
        # build the path to the XML file
        xml_path = os.path.join(root_path, item[0], item[1], 'record.xml')

        # parse the XML file
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # extract information from the XML file based on the column name
        column_name = item[2]  # use the third element of the tuple as the column name
        for elem in root.iter(column_name):
            column_value = elem.text

        # append the new column value to the list
        new_cols.append(column_value)

# save the updated dataframe to a new CSV file
df.to_csv('updated_data.csv', index=False)