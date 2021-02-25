"""

Description: Python MiniProject- Reading a input text file,
             searching for any 5 Keywords and printing the
             keyword (along with its preceding and following
             words) and the total occurrence count of it.
Author: Pushkar Antony
PS.No: 99003729
Email ID: pushkar.antony@ltts.com
Date of Creation: 23/02/2021

"""
import re

""" The Parent class is defined below. """


class SearchKeywords:
    def __init__(self):
        print("\n\t Welcome to keyword search program!\n")
        self.my_file = open("input.txt", "rt")
        self.cont = self.my_file.read()
        self.cont_new = re.split(r"\W+", self.cont)


""" A sub class inherits from the parent class below. """


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


""" Object definition and calling"""


object_keyword = InputKeyword()
object_keyword.find_keyword()
