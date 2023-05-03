import sqlite3
import pandas as pd
from datetime import datetime

# Define a function to load the data from the database
def load_data_from_db(db_connection, table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, db_connection)

# Define a function to save the data to the database
def save_data_to_db(df, db_connection, table_name):
    df.to_sql(table_name, db_connection, if_exists='replace', index=False)

# Establish a connection to your database
db_connection = sqlite3.connect('your_database.db')
table_name = 'job_offers'

# Load existing data from the database
existing_data = load_data_from_db(db_connection, table_name)

current_datetime = datetime.now()

for filename in filenames:
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

    # Merge the new data with the existing data
    combined_data = pd.concat([existing_data, data], ignore_index=True).drop_duplicates()

    # Save the combined data back to the database
    save_data_to_db(combined_data, db_connection, table_name)

    # Cleanup: delete the downloaded file
    os.remove(filename)

# Close the database connection
db_connection.close()
