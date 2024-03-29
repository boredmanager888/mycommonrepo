#!/bin/bash
#**************************************************************
# Date: 070823   (Expected Solution with 35 Lines of Code)    *
# Title: Caesar Cipher                                        *
# Status: Testing (In Progress / Testing / Working)           *
# One of the first known examples of encryption was used by   *
# Julius Caesar. Caesar needed to provide written             *
# instructions to his generals, but he didn’t want his        *
# enemies to learn his plans if the message slipped into      *
# their hands. As result, he developed what later became      *
# known as the Caesar Cipher.                                 *
# The idea behind this cipher is simple (and as a result, it  *
# provides no protection against modern code breaking         *
# techniques). Each letter in the original message is shifted *
# by 3 places. As a result, A becomes D, B becomes E, C       *
# becomes F, D becomes G, etc. The last three letters in the  *
# alphabet are wrapped around to the beginning: X becomes A,  *
# Y becomes B and Z becomes C. Non-letter characters are not  *
# modified by the cipher.                                     *
# Write a program that implements a Caesar cipher. Allow the  *
# user to supply the message and the shift amount, and then   *
# display the shifted message. Ensure that your program       *
# encodes both upper case and lowercase letters. Your program *
# should also support negative shift values so that it can be *
# used both to encode messages and decode messages.           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
alpha_low_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                  "j", "k", "l", "m", "n", "o", "p", "q", "r", 
                  "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_up_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                 "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                 "S", "T", "U", "V", "W", "X", "Y", "Z"]
ProcCtr = 0
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
MessageInOld = input("Enter your message here: ")
MessageInProc = MessageInOld
ShiftIn = input("Enter the pass key (numeric only): ")
cShiftIn = data_check(ShiftIn)
new_up_list = alpha_up_list[cShiftIn:] + alpha_up_list[:cShiftIn]
new_low_list = alpha_low_list[cShiftIn:] + alpha_low_list[:cShiftIn]
if icheck == 0:
  while ProcCtr != len(MessageInOld):
    char = MessageInOld[ProcCtr]
    if char in alpha_up_list:
      MsgPos = ProcCtr
      CharPos = alpha_up_list.index(char)
      MessageInNew = MessageInProc[:MsgPos] + new_up_list[CharPos] + MessageInProc[MsgPos + 1:]
      MessageInProc = MessageInNew
    elif char in alpha_low_list:
      MsgPos = ProcCtr
      CharPos = alpha_low_list.index(char)
      MessageInNew = MessageInProc[:MsgPos] + new_low_list[CharPos] + MessageInProc[MsgPos + 1:]
      MessageInProc = MessageInNew
    else:
      MsgPos = ProcCtr
      MessageInNew = MessageInProc[:MsgPos] + char + MessageInProc[MsgPos + 1:]
      MessageInProc = MessageInNew
    ProcCtr = ProcCtr + 1
  print("The coded/decoded message: ", MessageInNew)
print("Thank you for using this app.")
#**************************************************************