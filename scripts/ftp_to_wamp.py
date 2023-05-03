import ftplib
import pandas as pd
import config
import os
import wamp
import streamlit as st
from datetime import datetime


def main():
    """
    Main function to download and process CSV files from an FTP server, then upload the combined DataFrame to a WAMP server.
    """
    # FTP settings
    ftp = ftplib.FTP(config.FTP_ip)
    ftp.login(user=config.FTP_user, passwd=config.FTP_pw)

    # Get a list of filenames in the current directory on the FTP server
    filenames = ftp.nlst()
    current_datetime = datetime.now()
    print('Connected to the ftp server.')

    # Initialize an empty list to store DataFrames
    data_frames = []

    # Download and process each file from the FTP server
    for filename in filenames:
        # Download the file and save it locally
        with open(filename, 'wb') as file:
            ftp.retrbinary('RETR ' + filename, file.write)

        # Read CSV file into pandas DataFrame
        data = pd.read_csv(filename)

        # Convert "Date fin" column to datetime objects
        data['Date fin'] = pd.to_datetime(data['Date fin'])

        # Check if every "Date fin" value is older than the current datetime
        if (data['Date fin'] < current_datetime).all():
            # If true, skip this file and continue with the next one
            print(f"Skipping {filename} as all 'Date fin' values are older than the current datetime.")
            os.remove(filename)
            continue

        # Append the DataFrame to the list
        data_frames.append(data)

        # Cleanup: delete the downloaded file
        os.remove(filename)

    # Concatenate all the DataFrames into a single DataFrame
    combined_data = pd.concat(data_frames)

    # Upload the combined DataFrame to the WAMP server
    wamp.upload_df_to_wamp(combined_data)

    # Close the FTP connection
    ftp.quit()

if __name__ == "__main__":
    main()
