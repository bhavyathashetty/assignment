"""2.	Write a program to accept a two-dimensional array containing integers as the parameter 
and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row
Example:
Input:                                    
[[0 1 2 3]
 [3 4 5 5]
 [6 7 8 8]
 [9 0 1 9]]
Output:
	minimum value element in the array: 0
	maximum value element in the array: 9
	elements with minimum values column-wise: [0 0 1 3]
	elements with maximum values column-wise: [9 7 8 9]
	elements with minimum values row-wise: [0 3 6 0]
	elements with maximum values row-wise: [3 5 8 9]"""

import itertools

r = int(input("Enter Number of rows"))
c = int(input("Enter Number of columns"))

main_list = []

for i in range(r):
  temp_list = []
  for j in range(c):
    temp_list.append(input("Element {0}:{1}: ".format(i, j)))
  main_list.append(temp_list)

i = 0

for l in main_list:
    print(f"Max Of {i} th Row is : {max(l)}")
    i += 1

i = 0

for l in main_list:
    print(f"Min Of {i} th Row is : {min(l)}")
    i += 1
    
l=list(itertools.chain.from_iterable(main_list))

print(f"Max of all elements in list is {max(l)} and min is {min(l)}")