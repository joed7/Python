'''Python script for the demo of common string operations
'''

str = 'string demo!'

print str          # Prints complete string

print len(str)     #Prints string length

#Example of string indexing
print str[0]       # Prints first character of the string

#Example of string slicing
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character


#Example of string concatenation
print str + "TEST" # Prints concatenated string

#Find a character in string
print str.find('d') #finds the index of the first occurance of the given character/string beginning from left
