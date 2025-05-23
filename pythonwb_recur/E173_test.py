#!/bin/bash
#**************************************************************
# Date: 091324 (Expected Solution with 33 Lines of Code)      *
# Title: Run-Length Decoding                                  *
# Status: Testing (In Progress / Testing / Working)           *
#  Run-length encoding is a simple data compression technique *
# that can be effective when repeated values occur at         *
# adjacent positions within a list. Compression is achieved by*
# replacing groups of repeated values with one copy of the    *
# value, followed by the number of times that the value       *
# should be repeated. For example, the list ["A",             *
# "A","A","A","A","A","A","A","A","A","A","A","B","B", "B",   *
# "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed *
# as["A", 12, "B", 4, "A", 6, "B", 1] . Decompression is      *
# performed by replicating each value in the list the number  *
# of times indicated. Write a recursive function that         *
# decompresses a run-length encoded list. Your recursive      *
# function will take a run-length compressed list as its only *
# parameter. It will return the decompressed list as its only *
# result. Create a main program that displays a run-length    *
# encoded list and the result of decoding it.                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
final_list = []
#--------------------------------------------------------------
def decode_func(user_list, flist):
  #print("Entering New Loop:", len(user_list))
  if len(user_list) == 0:
    print("Exiting Function:", flist)
    return flist
  else:
    for i in range(user_list[1]):
      flist.append(user_list[0])
      #print(i, "Current Value:", flist)
    #print("Before Reduction:", len(user_list))
    for j in range(2):
      user_list.remove(user_list[0])
    #print("Remaining list is", len(user_list))
    decode_func(user_list, flist)
#--------------------------------------------------------------
if __name__ == "__main__":
  encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
  print("The encoded list is", encoded_list)
  print("The decoded list is", decode_func(encoded_list, final_list))
  print("Thank you for using this app.")
#**************************************************************