# In python, if statements are used to run any code or block of code if it holds true.

# eg:

if True:
    print("Printing this statement")  # this will be printed


if False:
    print("This wont be printed")    #this statement wont be printed.

# From above two examples, it is clear that only those statements that holds true will be executed by if statement.

# ===> How to know if a statement or block of statement is a part of "if" statement? The answer is that by looking at the indentation. Indentation is some spaces given, normally we give four spaces.

if True:
    print("This first line will be printed")
    print("this seconf line will also be  printed.")
    print("This third line will also be printed")

#In above line of code, all three print statements are inside the indentations of "if" statement so they all will be executed until and unless if statement holds true.

#########################################################################################################


# CHECK IF 3 IS EVEN OR ODD?

if(3%2==0):
    print("3 is even")   #present inside body of if , denoted by indentations
else:
    print("3 is odd")   #present inside body of else , denoted by indentations

# if "if" statement holds false and wont be executed, then else statement will run. The syntaxes for both if and else statement is as shown above. The indentations should be kept in mind.


'''In other languages like C, we used curly braces to specify scopes. But, in python, indentations does specify the scope of statements or does the work of the curly braces.'''

