# Creating a dictionary
dict1= {1:'Sudip', 2:'Trishna', 4:'Hari'}

#fetching values
print(dict1[2])   # gives Trishna as output
print(dict1.get(4))  #gives hari as output

#lets try to fetch values with keys not present. eg- key 3 is not present in above dictionary.

# print(dict1[3])  # it throws error as keyerror since key 3 is not present 

print(dict1.get(3))  # but when we use get fucntion in same case, we dont get error but 'None' as an ooutput since there is no any key as 3.

'''What if there is no key in the dictionary and you still want to print some value for it? ''' 

print(dict1.get(3,'No key found'))  # there is no key as 3 in our dictionary but still it will print the given line "No key found. This is one way of returning a data when you dont have a key"

