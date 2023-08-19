Module 2 Python Data Cleaning

import numpy as np
import pandas as pd
import module1 as m1

##Task 1: Drop the unwanted columns - This Python function, drop_columns(), renames the columns of a DataFrame m1, drops the columns 'PatientId', 'AppointmentID', and 'Neighbourhood' from the DataFrame, and returns the modified DataFrame with these columns removed.

def drop_columns():
    ds = m1.rename_columns()
    # Method to drop unnecessary columns from the DataFrame.
    ds.drop(["PatientId", "AppointmentID", "Neighbourhood" ], axis = 1, inplace=True)
    # Returns: DataFrame with specified columns dropped.
    return ds


##Task 2: Creating the new column - The create_bin() function, First drops the rows where the value in the 'Age' column is equal to 0. And generates age group labels(given) and categorizes the 'Age' values into bins with 20-year intervals. It uses the pd.cut() function from the pandas library to create an 'Age_group' column in the DataFrame.

def create_bin():
    ds = drop_columns()
    #First Drop rows with Age == 0
    ds=ds.loc[ds['Age']!=0]
    # Generating labels for age intervals (e.g., '1 - 20', '21 - 40', etc.)
    labels = ["{0} - {1}".format(i, i + 20) for i in range(1, 118, 20)]

    # Using the pd.cut() function to categorize ages into groups(use bins = range(1, 130, 20) ,right=False and use the given labels)
    ds['Age_group']=pd.cut(ds['Age'],bins=range(1,130,20),right=False,labels=labels)
    # Returning the modified dataset with assigned age groups
    return ds

##Task 3: Drop the column - the drop() function is used to streamline the process of removing the 'Age' column from the DataFrame containing age group information, and it returns the DataFrame ds without the 'Age' column, making it more focused on the categorized age groups for subsequent analysis.

def drop():
    ds = create_bin()
    # Method to drop the original 'Age' column from the DataFrame.
    ds = ds.drop(columns=['Age'])
    # Returns: DataFrame with the 'Age' column dropped.
    return ds

##Task 4: Convert the Noshow - the convert() function streamlines the process of converting the 'NoShow' column into a binary format, representing appointment attendance, and returns the DataFrame ds with this modified column for further analysis and modeling.
def convert():
    ds = drop()
    # Method to convert 'NoShow' values into binary values (1 for 'Yes' and 0 for 'No').
    ds['NoShow'] = ds['NoShow'].map({'Yes': 1, 'No': 0})
    # Returns: DataFrame with 'NoShow' column values converted to 1s and 0s.
    return ds


##Task 5 - Exporting the Cleaned Dataset- The function export_the_dataset() exports the cleaned DataFrame to a new CSV file named 'patients.csv'. It uses the pandas library to write the data to the CSV file.

The DataFrame obtained from the previous task is used as input and return the cleaned dataframe 'df'.

def export_the_dataset():
    df = convert()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv(r"patients.csv", index=False)
    return df


# TASK 6: Load the Cleaned dataset 'patients.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "patients"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project

