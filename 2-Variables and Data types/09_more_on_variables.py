# Here, we will be learning how memory is assigned to multiple variables pointing at a same value or multiple value.

a=10;  #a variable is created having value 10

# When we create a variable, in the background, there may have been a box named "a" inside which the data is 10 and variable "a" must be having some address too. Let us check what that address is.

print("ID a:",id(a))   #id(name_of_variable) gives the address of that variable

# Let, us create another variable "b" assigning the same data of a. In the background, we may think, another box "b" with value 10 and certain address is created.

b=a
print("Id b:",id(b)) #printing the id of b


# To our surprise, the address of a and b were not different but they had same memory address. 
# It is because, in python, if we have same data for multiple variables, then they will point to the same address. 
# Here, 2 boxes are not created for a and b, instead a single box with value 10 is created in which "a" and "b" variables are pointing at. 
# Because of this reason, python is a memory effiecient  language.

k=10
print("ID k:",id(k))  #here, k is also having same value 10, so it will also have the same address.


# Now, let us see, what happens if we overwrite the value of b from 10 to 20.

b=20  # value of b is no more 10 now.
print("Id of a:",id(a))  #same address as previous because it still has value 10 in it i.e no any change in address
print("Id of b:",id(b))  #its address is changed because it is holding a different value but not 10.
print("Id of k:",id(k))   #same address as previous because it still has value 10 in it i.e no any change in address

# Now, there are created 2 boxes in the memory. One for variable "a" and "k" and another for the variable "b"

a=9
k=a 
#  Now, a and k are pointing to another box with value 9. 
# What happened to the previous box with value 10 in it? it is now not being pointed by any of the variable.
#  In such case, that box will be later on garbage collected. i.e the memory which is not used or tagged by any variabe will be ready for garbage collection later.


############### HOW TO USE CONSTANTS IN PYTHON #############

# We know, the value for pi is 3.14. 

PI=3.14   
PI=3.5
# pi has specific value i.e 3.14 thats why pi is a constant in mathematics. 
# But, in python, here we can change the value of pi and changing to 3.5.
#  So, in python, there is no provision to make a value as constant.
#  if there was such provision, i would not have been able to change the value of pi from 3.14 to 3.5.
#  But, we can show our intention of declaring any variable as constant by writing the name of the variable in capitals as "PI" or "G" or anything. This is just referencing to programmer that "Hey, this is a constant, please dont change or modify its value"