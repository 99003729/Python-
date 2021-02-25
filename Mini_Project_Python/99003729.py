"""

Description: Python MiniProject- Reading a input text file, searching for 5 Keywords and printing the count,line
and words preceding and following it in a output text file.
Author: Pushkar Antony
PS.No: 99003729
Email ID: pushkar.antony@ltts.com
Date of Creation:23/02/2021

"""

import re  # importing regex


my_file = open("input.txt", "rt")  # opening the input text file from directory
cont = my_file.read()  # reading the input text file
cont_new = re.split(r"\W+", cont)  # using regex split the read input file free of special characters and whitespaces
n = int(input("\n Enter the number of keywords you want to search for: "))  # asking user for no of keywords.
c = 0  # initialising count for while loop as 0
while n > c:  # entering a while loop
    keyword = input("\n Enter the keyword you want to search for: ")  # asking user for keyword input
    file_name = keyword + ".txt"  # creating the output file name from user input
    out_file = open(file_name, "a+")  # output file created using append+(append + read)
    pattern = re.findall(keyword, cont, re.M | re.I)  # using findall regex to create a pattern for the keyword
    keyword_count = str(len(pattern))  # finding the length of the pattern and hence the keyword count
    for i in range(len(cont_new)):  # starting a 'for' loop to search index by index inside cont_new for the keyword
        if re.match(keyword, cont_new[i], re.M | re.I):  # checking if the keyword matches with any word inside cont_new
            out_file.write(" The keyword: " + keyword + " was found on this line --->  " +
                           cont_new[i-1] + " " + cont_new[i] + " " + cont_new[i+1] + "\n")  # writing the keywords
    out_file.write("\n -------------------------------------------------------------------------------------\n")
    out_file.write("\n The word count for the given keyword is: " + keyword_count)  # writing the keyword count
    out_file.close()  # closing the file
    c += 1  # incrementing the count by 1

# End of Code!
