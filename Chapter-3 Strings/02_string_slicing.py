name = "Sudip"
greeting= "Good Morning, "
print(type(name))


# 1)CONCATENATION OF TWO STRINGS
print(greeting+name)

#SLICING- It is done using the index that starts from 0 and goes to (length-1)
print(name[0])  #will slice S at index 0 in  string variable "name"
print(name[2])  # will slice d present at index 2 in string variable "name"
# print(name[5])   string index out of range error since indexing only goes upto 4( zero to length-1) in string variable "name"


#String object doesnt support item assignment. Lets see an example to understand it in more better way.

address= "Kathmandu"
# address[2]="m"  ---> This will not change character at index 2 i.e. t to "m" since string doesnt allow its object to be changed.

# 2) SLICING--> The first index is included and the last is excluded.
print(address[0:4])  #--> This will slice the string from index 0 to 3.
print(address[1:3])  #--> This will slice the string from index 1 to 2.
print(address[:4])   #---> if left first index blank, then it will automatically start from 0 i.e same as address[0:4]
print(address[0:])   # --> prints from 0 to last index.
print(address[:])   #---> Prints all the characters of the string.


'''
Negative indexing in string- Negative indexing starts from backward of string with index value -1 and goes like -2, -3, etc. eg- In "Sudip", p is at -1 index, i at -2 index, d at -3 index and so on. 
Why do we need to use negative indices? It is because sometimes, you dont know the length of string and you want to access the last character of the string, then directly -1 index can be used.
'''
print(address[-1])
print(address[-4:-1])   #--> This is same as address[5:]

# 3) SLICING WITH SKIP VALUE
'''We can provide a skip value as a part of our slice. Sometimes, we may want to skip some characters while slicing, so this technique comes handy in such situation. Skip value is given as third argument to the string'''

college="Nepal College of Information Technology"
print(college[0:10:1])  #---> This will print from index 0 to 9 but even indexes are only printed since skip value is 2.   O/p--> NplCl
print(college[::3])     #--> prints from index 0 to last but skip value here is 3.
