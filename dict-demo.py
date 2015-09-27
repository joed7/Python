'''Python script to demonstrate python dictionaries
'''

example_dict= {1:'one',2:'two',3:'three'} #initialize dictionary with initial values
example_dict[4] = "four"         #adding "Four" value for 4 keys

print example_dict[2]           # Prints value for 2 key
print example_dict          # Prints complete dictionary
print example_dict.keys()   # Prints all the keys
print example_dict.values() # Prints all the values

print 1 in example_dict #checks if 1 key exist in the dictionary         
