#**************************************************************
# Date: 011823 / 012623                                       *
# Title: Area of a Regular Polygon                            *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# A polygon is regular if its sides are all the same length   *
# and the angles between all ofthe adjacent sides are equal.  *
# The area of a regular polygon can be computed usingthe      *
# following formula, where s is the length of a side and n is *
# the number of sides:                                        *
#                          n x s^2                            *
#              Area = ----------------                        *
#                      4 x tan (pi/n)                         *
# Write a program that reads s and n from the user and then   *
# displays the area of aregular polygon constructed from these*
# values.                                                     *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import math

computed_value = 0
icheck = -1
while icheck == -1:
  iLength = input("What is the length of the sides? ==> ")
  iSides = input("How many sides does the polygon have? ==> ")
  try:
    ciLength = float(iLength)
    ciSides = float(iSides)
    icheck = 0
  except:
    print("Please input number data only.")
#--------------------------------------------------------------
computed_value = (ciSides * ciLength**2) / (4 * math.tan(math.pi/ciSides))
fcomputed_value = format(computed_value, '2f')
final_value = str(fcomputed_value)
#--------------------------------------------------------------
print("The area of the polygon is", final_value, "sq. units.")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.) Will this have the same result if used to compute the 
#     area of the triangle?
