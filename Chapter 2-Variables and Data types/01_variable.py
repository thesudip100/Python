'''VARIABLES AND DATA TYPES IN PYTHON 

1) None Data Type
2) Numeric- int,float,complex, bool
3) sequence- list, tuple, set,strings, range
4)Dictionaries/Mapping'''

# 1) STRING DATA TYPE
a = "Sudip"  #string; can be enclosed either in single, double or triple quote.

# Triple quote is used if you want to include double and single quote as a part of the string and also you can change the line when triple quote is present.

w='''Sudip's"s
is a
good
man'''  



# 2) NUMERIC DATA TYPE - consists of int, float, complex and bool

b = 367      #integer

c = 45.32    #floating point numbers

com= 5+ 6j  # complex data type
print(type(com))   # gives the data type as complex



# Variables are nothing but a container to store a value. Here, a, b, and c are variables which are storing string, integer value and floating point numbers. Python automatically detects the data type of the variable. We dont need to specify the data type in python.

# Data type tells the compiler about the type of variable; either it is float or double or string or anything else.

# Keywords are reserved words in python like def, class, False, True, in, is and,if, elif etc and it is not expected to use these keywords as a variable name.

print(a)
print(w)
print(b)
print(c)



#BOOLEANS DATA TYPE(returns either true or false)

d=True
print(d)


#3)NONE DATA TYPES - is used to denote nothing in python

e=None;
print(e);



#PRINTING THE TYPE OF VARIABLE
print(type(b))  #this will print the datatype of variable b.


# IDENTIFIERS are names given to class, function or variables.

# We can convert data type into complex as well.

p=5
q=6
print(complex(p,q))  #prints 5+6j

####################### RANGE #########################

# let us print values from 1 to 10.
ran=range(1,11)  # this has stored values from 1 to 10 in variable a.
print(type(ran))

# But, how to access these elements from 1 to 10? The better way is using for loop but we have not read for loop as of now, so we will access them using list.

print(list(ran))   # prints the values from 1 to 10 in list format.

# Can we print only even numbers from 1 to 10 using range? Yes,we can.

print(list(range(2,11,2)))   # starting value, end value, skip value is given inside the bracket.
