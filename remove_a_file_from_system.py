import os
myfile=input("Enter path")
# "C:/Users/nsoum/Documents/soumya.txt"

## If file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
    print("File Removed")
else:    ## Show an error ##
    print("Error: %s file not found" % myfile)