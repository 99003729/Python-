"""
Description: Python MiniProject- Reading a input text file, searching for 5 Keywords and printing the count,line
and words preceding and following it in a output text file.
Author: Pushkar Antony
PS.No: 99003729
Email ID: pushkar.antony@ltts.com
Date of Creation:23/02/2021
"""
import re


my_file = open("input.txt", "rt")  # opening the input text file from directory
cont = my_file.read()  # reading the input text file
n = int(input("\n Enter the number of keywords you want to search for: "))  # asking user for no of keywords.
c = 0  # initialising the count as 0
while n > c:  # entering a while loop
    keyword = input("\n Enter the keyword you want to search for: ")  # asking user for keyword input
    file_name = keyword + ".txt"
    out_file = open(file_name, "a+")
    pattern = re.findall(keyword, cont, re.M | re.I)
    keyword_count = str(len(pattern))
    for i in pattern:
        out_file.write(i + "\n")
    out_file.write("\n The word count for the given keyword is " + keyword_count)
    out_file.close()
    c += 1
