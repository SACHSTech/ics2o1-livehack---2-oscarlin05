"""
------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  a program that computes if the detected life form is which type of Martian class or not. 
 
Author: Lin.O
 
Created: 23/02/2021
------------------------------------------------------------------------------
"""
print("****** Perserverance Martian Class Detector ******")

#get the number of eyes and antennas 
antenna = int(input("How many antennas? "))
eyes = int(input("How many eyes? "))

#compute and output 
if antenna >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")
elif antenna <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")
if antenna <= 2 and eyes <= 3:
  print("Life form detected: BrooklynMartian")
if antenna == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")
else:
  print("No life form detected")
