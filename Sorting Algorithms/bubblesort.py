"""
This script provides a function to sort an array of numbers in ascending order using the bubble sort algorithm
"""
import random

def bubblesort(arr):
  # Calculate the length of the array and assign it to variable n
   n = len(arr)
   switched = True
   # This while loops continue as long as elements in the array are being switched.
   # The algorithm knows it is complete when it runs through the array of numbers successfully without
   # switching any numbers.  
   while switched == True:
     switched = False
     # Iterate through the array of numbers element by element (we will finish at the second last element
     # because we are comparing the current element with the next element in the array).
     for i in range(n-1): 
       # Take the first two elements and compare them. If the first number is > the second number then switch.
       if arr[i] > arr[i+1]:
         buf = arr[i]
         arr[i] = arr[i+1]
         arr[i+1] = buf
         switched = True


# variable containing array of numbers:
numbers = [0 for i in range(50)]

# this initialises the array ('numbers') with randomly generated numbers from 0 to 99 
count = 0
print("Numbers: ", end = "")
while count < 50:
  numbers[count] = random.randrange(0, 100)
  print(str(numbers[count]), end = ",")
  count += 1
print("")

bubblesort(numbers)


# Verification print
count = 0
print("Sorted?")
print("Numbers: ", end = "")
while count < 50:
  print(str(numbers[count]), end = ",")
  count += 1