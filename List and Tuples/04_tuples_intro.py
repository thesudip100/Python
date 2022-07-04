'''Tuples are the collection of data inside the small parentheses and immutable.

The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

If tuples cannot be changed, then why to use them? It is because they are faster than lists and prevents from any accidental modification in the program.'''

# CREATION OF TUPLES

tuple1= (1,2,"Sudip","Ishan",5,8,10)
print(tuple1)

tuple2= ()   #empty tuple
tuple3=(1,)  #Tuple with single value should be declared with comma at the end.if comma not given, then it will act like value 1 is assigned to tuple3 which is integer but not a tuple is assigned to tuple3.
tuple4=(1,2,3)  #tuple with multiple values
print(tuple3)