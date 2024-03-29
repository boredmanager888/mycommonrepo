#!/bin/bash
#**************************************************************
# Date: 110323 (Expected Solution with 43 Lines of Code)      *
# Title: Formatting a List                                    *
# Status: Testing (In Progress / Testing / Working)           *
# When writing out a list of items in English, one normally   *
# separates the items with commas. In addition, the word      *
# “and” is normally included before the last item, unless the *
# list only contains one item. Consider the following four    *
# lists: apples apples and oranges apples, oranges and        *
# bananas apples, oranges, bananas and lemons Write a         *
# function that takes a list of strings as its only           *
# parameter. Your function should return a string that        *
# contains all of the items in the list formatted in the      *
# manner described previously as its only result. While the   *
# examples shown previously only include lists containing     *
# four elements or less, your function should behave          *
# correctly for lists of any length. Include a main program   *
# that reads several items from the user, formats them by     *
# calling your function, and then displays the result         *
# returned by the function.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
word_list = []
user_word = " "
#--------------------------------------------------------------
def word_list_fmt(str_list):
  str_list_fmt = ""
  ctr = 0
  while ctr <= len(str_list) - 1:
    if len(str_list) == 1:
      str_list_fmt = str_list[ctr]
      break
    elif len(str_list) == 2:
      str_list_fmt = str_list[0] + " and " + str_list[1]
      break
    else:
      if ctr == len(str_list) - 2:
        str_list_fmt += str_list[ctr] + " and " + str_list[ctr + 1]
        break
      else:
        str_list_fmt += str_list[ctr] + ", "
    ctr += 1
  return str_list_fmt
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_word != "":
    user_word = input("Enter a word: ")
    if user_word != "":
      word_list.append(user_word)
  print("Formatted List:", word_list_fmt(word_list))
  print("Thank you for using this app.")
#**************************************************************