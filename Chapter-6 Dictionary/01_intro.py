'''Let us learn something about dictionary now.

In lists and tuples, you were accessing the elements by using the index number that were assigned as 0,1,2,3,4,5. This indexing was done automatically by the computer.

But, in dictionary, you use key-value pair. You give a key to your value and access the value using that particular key. 

Key here acts like the index and value is the data to be fetched. Because we can assign our own key to a value, it becomes much easier and reiable to understand where the data is located and what kind of data is located.

For eg- dictionary_name[key_name] is the syntax that we use to fetch the data of that particular key.'''

'''   CREATING A DICTIONARY   ''' 

# We need to create a dictionary inside the curly braces by using the key value pair. Keep in mind, that every key should be unique and immutable.

dict= {"Sudip":"Redmi","Trishna":"Oneplus","Ram":"Apple"}

# Here, we have declared a dictionary in which the key are Sudip, Trishna and Ram and the values are the mobile phones they use i.e. Redmi, Oneplus and Apple.


'''    ACCESSING A DICTIONARY '''

# Now, let us try to access the value inside the dictionary using the key associated to them.

print(dict["Sudip"]) # this will print Redmi since the value associated with key "Sudip" is "Redmi".
 
'''
Instead of indexing 0,1,2,3... as key, using our own index has made it much easier to handle and look up for data.

There is another way to access the element of dictioary as well using get() fucntion.
'''
print(dict.get("Trishna"))  #this will print oneplus