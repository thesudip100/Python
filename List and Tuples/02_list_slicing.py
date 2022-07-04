# SLICING IN LIST

# Like in strings, the elements of list can also be sliced. Let us see how it can be done.

values=["Sudip","Ishan",42,25]

#In the above list, Sudip is at index 0, Ishan is at index 1, 42 at 2 and 25 at index 3.
print(values[1])
print(values[0:4])  #this will print elements at index 0,1,2,3.
print(values[0:])   #prints all the elements from index 0 upto last index.
print(values[:-1])  #prints all the elements except element at last index i.e -1.