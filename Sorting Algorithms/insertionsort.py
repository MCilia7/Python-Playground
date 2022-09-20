"""
This script provides a function to sort an array of numbers in ascending order using the insertion algorithms
"""

def insertionSort(arr):
  # Iterate through the array of numbers element by element (we will start at the second element
  # because we will be pushing the current element to the front as long as the previous element
  # of the array is greater than the current one).
  for i in range(1,len(arr)):
    buff = arr[i]
    j = i-1
    # Move the current element to the front of the array as long as it's not in the front
    # and the previous element is greater than the current one
    while j>=0 and buff < arr[j]:
      arr[j +1] = arr[j]
      # Move the greater elements one position up to make space for the swapped element.  
      j -= 1
      arr[j+1] = buff

# Create an array of numbers and assign it to the variable arr
arr = [12, 15, 62, 34, 1, 23, 19, 10, 41, 30, 51, 34, 17, 42, 67, 2, 7, 13, 18, 54, 0]
# Call the function insertionSort with the created array (arr)
insertionSort(arr)

# Print the result of the array
for i in range(len(arr)):
    print(arr[i])