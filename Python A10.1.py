# Tanner Zanga
# 11/2/2021
# Assignment 10.1

import os.path

print("Please use the following format for the next step. C:/Users/Username/... etc.")

print("")

filePath = input("Please enter the name of the directory you would like to place your file: ")

if not os.path.exists(filePath):
    os.makedirs(filePath)

fileName = input("What is the name of the file: ")

fullName = os.path.join(filePath, fileName+".txt")

file1 = open(fullName, "w")

line1 = input("Please enter your full name: ")
line2 = input("Please enter your address: ")
line3 = input("Please enter your phone number: ")

file1.writelines([line1, ", ", line2, ", ", line3])

file1.close()

test = open(fullName, "r")
print(test.read())