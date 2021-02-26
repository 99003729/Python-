"""

Description: Python MiniProject- Reading a input text file,
             searching for any number of Keywords and printing the
             keyword (along with its preceding and following
             words) and the total occurrence count of it.
Author: Pushkar Antony
PS.No: 99003729
Email ID: pushkar.antony@ltts.com
Date of Creation: 23/02/2021

"""
import re

""" The Parent class is defined below.(Using Classes)

 line 28: opening the input text file from directory
 line 29: reading the input text file
 line 30: using regex split the read input file free of
 special characters and whitespaces

"""


class SearchKeywords:
    def __init__(self):
        print("\n\t Welcome to keyword search program!\n")
        self.my_file = open("input.txt", "rt")
        self.cont = self.my_file.read()
        self.cont_new = re.split(r"\W+", self.cont)


""" A sub class inherits from the parent class below. (Using Inheritance)

 line 54: initialising count for while loop as 0
 line 55: asking user for no of keywords.
 line 56: entering a while loop
 line 57: asking user for keyword input
 line 58: creating the output file name from user input
 line 59: output file created using append+(append + read)
 line 60: using findall regex to create a pattern for the keyword
 line 61: finding the length of the pattern and hence the keyword count
 line 62: starting a 'for' loop to search index by index inside cont_new
 line 63: checking if the keyword matches with any word inside cont_new
 line 64: writing the keywords
 line 70: writing the keyword count
 line 71: closing the file
 line 73: incrementing the count by 1
"""


class InputKeyword(SearchKeywords):
    def find_keyword(self):
        c = 0
        n = int(input("\n Enter the no. of keywords you want to search for: "))
        while n > c:
            keyword = input("\n Enter the keyword you want to search for: ")
            file_name = keyword + ".txt"
            out_file = open(file_name, "a+")
            pattern = re.findall(keyword, self.cont, re.M | re.I)
            keyword_count = str(len(pattern))
            for i in range(len(self.cont_new)):
                if re.match(keyword, self.cont_new[i], re.M | re.I):
                    out_file.write(" The keyword: " + keyword +
                                   " was found on this line --->  " +
                                   self.cont_new[i - 1] + " " +
                                   self.cont_new[i] + " " +
                                   self.cont_new[i + 1] + "\n")
            out_file.write("\n -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
            out_file.write("\n The word count for the given keyword is: " +
                           keyword_count)
            out_file.close()
            c += 1


""" Object definition and calling

line 83: defining an object keyword
line 84: calling main program using object.method
"""


object_keyword = InputKeyword()
object_keyword.find_keyword()


""" END OF PROGRAM"""
