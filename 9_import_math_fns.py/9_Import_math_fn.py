'''In this session, we will learn to import modules and use its function.
We can find a square of a number manually as below:'''

a= 2**4  # this means 2 to the power 4 i.e 16
print(a)  

# But, same thing can be done using the modules and its function then why to do manually? . For this, we need to import math module. Some of the functions inside math module are pow(), sqrt(), sin(),cos(),factorial(), log(), etc.


#  SOME BASIC FUNCTIONS OF MATH MODULE
'''
a) math.cos()	Returns the cosine of a number

b) math.factorial()	Returns the factorial of a number

c) math.pow()	Returns the value of x to the power of y

d) math.sqrt()	Returns the square root of a number

e) math.sin()	Returns the sine of a number

f) math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
'''

# print(pow(2,3))    ---> this line will throw error since pow() function is inside math module and we havent still imported math module yet , so until and unless we import that module, we cannot use its functions.



###########################################################################################



################# IMPORTING MODULE #############

import math   #here math is module name which has got all these math functions.

print(math.sqrt(25))  #since we have imported math function, now we can use sqrt() function and it will give output as 5. Remember, We need to use functions inside the module using module_name.fn_name() eg. math.pow(2,4)  --> 16

print(math.floor(2.9))  #prints lower value i.e. 2
print(math.ceil(2.2))  # prints upper value i.e. 3

#floor() and ceil() are not like roundoff. When we use floor, it simply means to print the lower value i.e 3 even if it is 3.9. And when we use ceil(), it means to print upper value i.e 4 even if it is 3.1.

print(math.factorial(5))   #this gives factorial of 5 i.e 5*4*3*2*1=120

print(math.pow(3,2))   # this means 3 square 2 i.e 9






#########################################################################################

############ PRINTING VALUES OF CONSTANTS #########

'''Using math module, we can even print the values of constants. for eg: '''

print(math.pi)  #prints the value of pi i.e 3.1415  
print(math.e)  #prints the value of epsilon i.e 2.71828



###########################################################################################


# The names of the module may be large in some case and we are way to lazy to type the full name of the module in such scenario. For such case, we can use below method and import module as our desired name. This is a concept of using "Allies"

import math as m

print(m.sqrt(25))  # here, we imported our math module as "m", so now instead of writing "math" everytime, we can simply write "m" which saves our time, make it easy as well.

# We can also use math.sqrt(25) also in this case too.


###############################################################################################


'''In math module, there are many functions and the moment you say, import math, everything will be imported. But, what if you dont want all functions but some specific ones? We can do it this way. Let us import sqrt and pow() functions only from math module'''

from math import pow,sqrt
print(pow(2,3))    # prints 8
print(sqrt(49))    #  prints 7

#when we import specific function, there is no necessity to do math.pow() but we can directly use the function without using dot operator in this case.