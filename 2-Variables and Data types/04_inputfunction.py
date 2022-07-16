'''Input function is used to take any input from the user. This function only takes input in the form of string even though you are asking for numeric input, so typecasting needs to be done.'''

a=input("Enter your name:")
print(a)

b=input("Enter a number:")
print(b)
print(type(b))    #even though we took numeric value as input, its type will be string since every input is string using input() func.

#TYPECASTING TO TAKe INPUT
c=int(input("Enter a number: "))
print(c)
print(type(c))
print(c+43)

'''
Here, we typecasted the input of c into an integer input, so addition of integer values are possible. Typecasting is done, if only possible. eg. You input Sudip and asking to typecast into integer, which is not possible.
'''