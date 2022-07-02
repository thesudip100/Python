s="32"   
#you may think that s is a integer storing variable but since 32 is enclosed inside double inverted comma, s is storing string   literal.But, we can change this string  literal into integer using type casting.
print(type(s))

# print(s+5)    holds error since s(string) and 5(integer) cant be added

a=int(s)
print(type(a))
print(a+3)  #s has been converted to integer and its value is being holf by a, so it is posibble to add integer and integer value 3.

#Here, 32 string literal can be a valid integer if converted but not everything can be converted into valid integers. eg, if you have "SUDIP" as an string and you want to convert this into an integer, then it cant lead to any valid integer value. So, typecasting only tries to change the data type, but it is not necessary that it will 100% typecast the data from one form to other form i.e no guarantee.

'''
WHAT ACTUALLY IS TYPECASTING?
TYPECASTING IS THE WAY TO CONVERT ONE DATA TYPE INTO OTHER.
'''

