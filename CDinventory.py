#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------#
# Title: CDInventory.py
# Desc: Program to add CD information to a text file. Also display titles from sheet and want to be added
# Change Log: (Who, When, What)
# EPales - 11/13/2022 - Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('Write or Read file data.')
while True:
    print('\n[1] add data to list\n[2] to write data to file\n[3] to read data from file')
    print('[4] display data\n[0] to quit')
    strChoice = input('1, 2, 3, 4, or 0: ') #
    print('\n\n')

    if strChoice == '0':
        break
    if strChoice == '1':  # no elif necessary, as this code is only reached if strChoice is not '1'
        # Add data to list in memory 
        strID = input('Enter an ID: ')
        strAlbu = input("What is the album title?: " )
        strName = input('What is the name of the artist?: ')
        dicRow = {"ID": strID, "Album": strAlbu, "Artist": strName}
        lstTbl =['strID' + 'strAlbu' + 'strName']
        lstTbl.append([])
        pass
    elif strChoice == '2':
        # List to File
        print("Saving Inventory to File" '\n')
# 4. Save the data to a text file CDInventory.txt if the user chooses so
        text_file = open("CDInventory.txt", "a+")
        text_file.writelines(dicRow)
        text_file.writelines('\n')
        text_file.writelines(str(strID) + '\t|')
        text_file.writelines(strAlbu + '\t\t|' + '\t')
        text_file.writelines(strName + '\n')
        text_file.close()
        
        pass
    elif strChoice == '3':
        # File to print
        print("Viewing Current Inventory" '\n')
# 3. Display the current data to the user each time the user wants to display the data
        text_file = open("CDInventory.txt", "r")   
        whole_thing = text_file.read()
        print(whole_thing)
        text_file.close()
        pass
    elif strChoice == '4':
        # Display data from question 1
        print("ID" + '\t' "Album" + '\t' "Artist")
        print(f"{dicRow['ID']}, {dicRow['Album']}, {dicRow['Artist']}")
        
        
        
        pass
    else:
        print('Please choose either 1, 2, 3, 4 or 0!')