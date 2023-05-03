import ftplib
import os
from datetime import datetime

def display_csv(csv_file) :
    ftp = ftplib.FTP('192.168.1.116')
    ftp.login(user='user', passwd='test123')

    filename = csv_file
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR ' + filename, file.write)

    stat = os.stat(filename)
    size = stat.st_size
    mod_time = datetime.fromtimestamp(stat.st_mtime)
    permissions = oct(stat.st_mode & 0o777)  # convert decimal mode to octal string

    print(f"Permissions: {permissions}, Size: {size}, Modified: {mod_time}, Filename: {filename}")
