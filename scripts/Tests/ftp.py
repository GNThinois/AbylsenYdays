import ftplib
import streamlit as st
import pandas as pd
import config
import os
import wamp

# FTP settings
ftp = ftplib.FTP(config.FTP_ip)
ftp.login(user=config.FTP_user, passwd=config.FTP_pw)

# Get a list of filenames in the current directory on the FTP server
filenames = ftp.nlst()

print('ok')

# Streamlit app
st.title('FTP Data Display')

# Select file to display
filename = st.selectbox('Select a file to display', filenames)

# Download file from FTP server
with open(filename, 'wb') as file:
    ftp.retrbinary('RETR ' + filename, file.write)

# Read CSV file into pandas DataFrame
data = pd.read_csv(filename)

# Display DataFrame in Streamlit
st.write('### Offre:')
for column in data.columns:
    st.write(f'#### {column} : {data[column][0]}')

# Upload each row to WAMP server
for index, row in data.iterrows():
    wamp.upload_row_to_wamp(row)

# Cleanup: close FTP connection and delete downloaded file
ftp.quit()
os.remove(filename)
