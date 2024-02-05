import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import datetime
from datetime import datetime, timezone


def read_csv_files(folder_path):
    """
    Read every CSV file in a folder and create a DataFrame for each with the same name as the CSV file.

    Parameters:
    - folder_path (str): The path to the folder containing the CSV files.

    Returns:
    - dataframes (dict): A dictionary where keys are file names and values are corresponding DataFrames.
    """
    dataframes = {}

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith(".csv"):
            # Create the full path to the CSV file
            file_path = os.path.join(folder_path, file_name)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Use the file name (without extension) as the DataFrame key
            key = os.path.splitext(file_name)[0]

            # Add the DataFrame to the dictionary
            dataframes[key] = df

    return dataframes

def write_csv(dataframe, folder_path, file_name):
    """
    Write a DataFrame to a CSV file in the specified folder.

    Parameters:
    - dataframe: pandas DataFrame
    - folder_path: str, path to the folder where the CSV file will be saved
    - file_name: str, name of the CSV file
    """
    # Ensure the folder exists, create it if not
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the full path to the CSV file
    file_path = os.path.join(folder_path, file_name)

    # Write the DataFrame to CSV
    dataframe.to_csv(file_path, index=False)

    return print(f"{file_name} written succesfully at {file_path}")

def calculate_years_difference(dataframe, date_column):
    # Convert date_column to datetime format and make it timezone-aware
    dataframe[date_column] = pd.to_datetime(dataframe[date_column]).dt.tz_localize('UTC')

    # Get the current date and time in UTC
    current_date_time = datetime.now(timezone.utc)

    # Make the current_date_time timezone-aware
    current_date_time = current_date_time.replace(tzinfo=timezone.utc)

    # Calculate the difference in years
    dataframe['difference_in_years'] = (current_date_time - dataframe[date_column]).dt.days // 365

    return dataframe
    