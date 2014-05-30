import ftplib
import os
filenames = ['data_10.txt', 'data_11.txt','data_12.txt', 'scholarship.txt']
for filename in filenames:
    ftp = ftplib.FTP("reach121.com")
    ftp.login("avi12345", "Avi@12345")
    os.chdir(r"C:\\Avi Kapoor\\Python_Reach_1_To_1")
    myfile = open(filename, 'r')
    ftp.storlines('STOR ' + filename, myfile)
    myfile.close()
