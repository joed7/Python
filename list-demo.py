''' Python script demonstrating basic list operations
'''

list1 = [ 'dep1', 'dep2','dep3' ] # A list of same data types
list2 = [123, 'john'] # A list with multiple data-types
list3 = ['Java','C++',['Java Script','Html','CSS']] # List inside a list

print list1          # Prints complete list
print len(list1)     # Prints length of list1  
print list1[0]       # Prints first element of the list
print list1[1:3]     # Prints elements starting from 2nd till 3rd 
print list1[2:]      # Prints elements starting from 3rd element

print list1 + list2 # Prints concatenated lists

print 'dep1' in list1 #checking if element exist in list
