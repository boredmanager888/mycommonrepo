#!/bin/bash
#**************************************************************
# Date: 082424 (Expected Solution with 36 Lines of Code)      *
# Title: Run-Length Encoding                                  *
# Status: In Progress (In Progress / Testing / Working)       *
#  Write a recursive function that implements the run-length  *
# compression technique described in Exercise 173. Your       *
# function will take a list or a string as its only para-     *
# meter. It should return the run-length compressed list as   *
# its only result. Include a main program that reads a string *
# from the user, compresses it, and displays the run-length   *
# encoded result. Hint: You may want to include a loop inside *
# the body of your recursive function.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
fin_list = []
#--------------------------------------------------------------
def exp_list(input_lst, flist):
  count = 1
  print("Start Length:", len(input_lst))
  if len(input_lst) == 0 or len(input_lst) == 1:
    return flist
  elif input_lst[0] == input_lst[1]:
    for i in range(len(input_lst) - 1):
      if input_lst[i] == input_lst[i+1]:
        count += 1
      else:
        print("flist Before Append:", flist)
        print("input_lst Before Append:",input_lst[count:])
        flist.append(input_lst[count-1])
        flist.append(count)
        print("flist Before Recursion:", flist)
        print("input_lst Before Recursion:",input_lst[count:])
        exp_list(input_lst[count:], flist)

if __name__ == "__main__":
  user_input_lst = input("Enter a charater list: ")
  print(user_input_lst)
  in_list = [item.strip() for item in user_input_lst.split(',')] 
  print("User Input:", in_list)
  print("The compressed list is: ", exp_list(in_list, fin_list))
  print("Thank you for using this app.")