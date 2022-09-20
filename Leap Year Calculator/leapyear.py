#This script will ask the user to input a year and then tell the user if it is a leap year or not

#we need a number from the user to use it as a year 
year = int(input("Year: "))

"""
now we need to check if this is a leap year

conditions for leap year and common year
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)"""

if year%4 == 0 and 0 != year%100 :
   print ("leap year")
elif year%4 == 0 and year%100 == 0 and year%400 == 0: 
   print ("leap year")
else:
   print("common year")
