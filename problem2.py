"""
------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  a program that calculates the side of the shape if it is a triangle or not.
 
Author: Lin.O
 
Created: 23/02/2021
------------------------------------------------------------------------------
"""
print("****** Triangle Calcualtor ******")

#get the three lengths of the triangle
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

#compute 
if side1 >= side2 and side1 >= side3:
  largest = side1
  othersides = side2 + side3
elif side2 >= side1 and side2 >= side3:
  largest = side2
  othersides = side1 + side3
elif side3 >= side1 and side3 >= side2:
  largest = side3
  othersides = side2 + side1

#output 
if largest > othersides:
  print("The figure is NOT a triangle.")
else:
  print("The figure is a triangle.")
