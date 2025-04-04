#!/bin/bash
#**************************************************************
# Date: 073024 (Expected Solution with 56 Lines of Code)      *
# Title: Words with Six Vowels in Order                       *
# Status: Testing (In Progress / Testing / Working)           *
#  There is at least one word in the English language that    *
# contains each of the vowels a,e,i,o,u and y exactly once and*
# in order. Write a program that searches a file containing a *
# list of words and displays all of the words that meet this  *
# constraint. The user will provide the name of the file that *
# will be searched. Display an appropriate error message and  *
# exit the program if the user provides an invalid file name  *
# or if something else goes wrong while searching for words   *
# with six vowels in order.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_letter_check(data_input):
  ltr_set = ["a", "e", "i", "o", "u", "y"]
  org_ltr_set = ["a", "e", "i", "o", "u", "y"]
  tmp_ltr_set = []
  with open(data_input, "r") as f:
    file_data = f.readlines()

  for idx1, line in enumerate(file_data):
    temp_ltr_lst = list(line)
    for idx2, ltr in enumerate(temp_ltr_lst):
      if ltr in ltr_set:
        tmp_ltr_set.append(ltr)
        ltr_set.remove(ltr)
    if len(ltr_set) == 0 and tmp_ltr_set == org_ltr_set:
      print("Line:", idx1 + 1, " --> ", line)
    ltr_set = []
    tmp_ltr_set = []
    ltr_set = ["a", "e", "i", "o", "u", "y"]
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input("Please enter the file location: ")
  file_name = input("Please enter the file name: ")
  input_data = file_loc + file_name
  func_letter_check(input_data)
  print("Thank you for using this app.")
#**************************************************************