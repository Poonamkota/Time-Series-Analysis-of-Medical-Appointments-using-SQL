#Module 1 Python Data Cleaning & Exporting CSV file

import numpy as np
import pandas as pd
from datetime import datetime

##Task 1: Load the data : Read the patients data using 'Hospital_patients_datasets.csv' through pandas library and return the dataset for the further analysis.
def read_csv():
    # Method to read the CSV file "Hospital_patients_datasets.csv" using pandas.
    ds = pd.read_csv("Hospital_patients_datasets.csv")
    # Returns: Pandas DataFrame containing the data from the CSV file.
    return ds

##Task 2: Find the Duplicate Values - Here, We need to check for duplicate values in a dataset 'Hospital_patients_datasets'. Finally, the counts of duplicated values are returned as a integer. This information can be useful in identifying duplicate data and deciding on appropriate strategies to deal with them, such as imputation or deletion.

def check_duplicates():
    ds = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    count_dup = ds.duplicated().sum()

    # Returns: The number of duplicated rows found in the DataFrame.
    return count_dup


##Task 3:Find the null values - The function check_null_values() , calculates the sum of null (missing) values for each column in the DataFrame. It then returns a Series containing the count of null values for each column in the DataFrame. This provides insights into the presence and extent of missing data in the dataset after duplicates have been dropped.


def check_null_values():
    ds = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    check_null = ds.isna().sum()
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.

    return check_null

##Task 4: Convert the data type - The converting_dtype() function reads a dataset from a CSV file, converts the 'ScheduledDay' and 'AppointmentDay' columns to pandas datetime objects with date-only information, and returns the modified dataset.

def converting_dtype():
    ds = read_csv()
    # Method to convert 'ScheduledDay' and 'AppointmentDay' columns to datetime objects.
    ds['ScheduledDay'] = pd.to_datetime(ds['ScheduledDay'], utc=False).dt.strftime('%Y-%m-%d')
    ds['AppointmentDay'] = pd.to_datetime(ds['AppointmentDay'], utc=False).dt.strftime('%Y-%m-%d')
    # Returns: DataFrame with 'ScheduledDay' and 'AppointmentDay' columns converted to datetime objects.
    ds['ScheduledDay'] = pd.to_datetime(ds['ScheduledDay']) # Convert to datetime64[ns]
    ds['AppointmentDay'] = pd.to_datetime(ds['AppointmentDay']) # Convert to datetime64[ns]
    return ds
    
    
##Task 5: Renaming the columns - The rename_columns() function renames specific columns ('Hipertension' to 'Hypertension', 'Handcap' to 'Handicap', 'SMS_received' to 'SMSReceived', 'No-show' to 'NoShow'), and returns the modified dataset.

def rename_columns():
    ds = converting_dtype()
    # Method to rename some columns in the DataFrame.
    ds.rename(columns = {'Hipertension':'Hypertension', 'Handcap':'Handicap', 'SMS_received':'SMSRecevied', 'No-show':'NoShow'}, inplace = True)
    # Returns: DataFrame with certain column names changed to new names.
    return ds
