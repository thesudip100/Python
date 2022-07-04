# LIST METHODS IN PYTHON

# We can use certain inbuilt functions in python and operate on lists in easy manner.
# Some of the functions used in python lists are shown below:

list1= [4,1,8,3,6,2,9]
'''
list1.sort()   # this will sort the list in ascending order and update the list "list1" by itself.
list1.append(10)  # this will add value 10 at the last index and update the list "list1" by itself.
list1.insert(2, 24) # this will insert the value 24 at index 2 ( inserts not replace) and update the list "list1" by itself.
list1.reverse()     # this will reverse the list and update the list "list1" by itself.
list1.pop()     # this will delete the last index value and update the list "list1" by itself.
list1.pop(2)     # this will delete the index value at 2nd index and update the list "list1" by itself.

'''

list1.remove(8)  # this will remove the given value 8 from the list and auto updates the list.
print(list1)