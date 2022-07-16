'''Here, we will learn to create dictionary with the help of lists.

Let us create two lists as keys and values.'''

keys = ["Sudip","Trishna","Ram"]
values = ["Python","Java","C++"]





#Now, let us try to MERGE these two lists into a dictionary.

dict2=dict(zip(keys,values))  # here , we zipped the keys and values list and then converted into dictionwry using "dict" keyword
print(dict2)  #this will print keys and values in dictionary format.This is how, we can turn two lists into dictionary.





# Lets, try to add new key value pair in the dictionary. eg- Hari loves Javascript. Lets, try to add it in our dictionary. Hari as key is not present in the dictionary.

dict2["Hari"]="Javascript"
print(dict2)  #this will print updated dictionary with hari:Javascript also present.






#  Can we delete values from dictionary?? Suppose, I want to delete Sudip from this dictionary

del dict2["Sudip"]  #this will delete "Sudip:Python" from the dictionary.
print(dict2)  # no Sudip present.





#### ADDING DICTIONARY INSIDE A DICTIONARY AND VALUES AS LIST FOR A PARTICULAR KEY.


data= {'Sudip':'Python','Hari':'Javascript','Trishna':['Python','C++','C','HTML'],'Ram':{'Ram1':'Ruby language','Ram2':'Swift'}}

#here, we have put list ['Python','C++','C','HTML'] and dictionary {'Ram1':'Ruby language','Ram2':'Swift'} inside the dictionary named 'data'.

print(data) # this will print the 'data' dictionary.

print(data['Trishna'])  # gives ['Python','C++','C','HTML']

# We can also move inside the list like this.
print(data['Trishna'][1])  # gives C++ as an output.

print(data['Ram'])  # gives dictionary  {'Ram1':'Ruby language','Ram2':'Swift'}

print(data['Ram']['Ram2'])  # gives Swift
