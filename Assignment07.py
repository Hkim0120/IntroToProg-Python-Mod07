#------------------------------------------#
# Title: Assignment 07
# Description: Working with Pickling and Error Handling
# ChangeLog (Who,When,What):
# Hyungu Kim 5.31.2023 Created the script
#------------------------------------------#

import pickle # Import code from another file

Project_Title = "What is you hobby?"
print(Project_Title)
customer_name = str(input("Full Name: "))
customer_hobby = str(input("Hobby: "))
customer_list = [customer_name, customer_hobby]
print(customer_list)

# Store with pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(customer_list, objFile)
objFile.close()

# Read with pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)

# Demo 3
try:
    f = open("AppData.datZ", "rb")
except FileNotFoundError as e:
    print("Please check that the file exists!")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was an error!")
    print(e, e.__doc__, type(e), sep='\n')
