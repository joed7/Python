
#Python variables and data types

Variables are reserved memory locations to store values. This means that when we create a variable you reserve some space in memory. Depending on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.        
Values can be assigned to variables with equal sign `=`.  

  ```
  year=2015  #integer assignment
  month='august' #string assignment  
  salary=160.05 #float assignment
  ```
The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable

  __Data Type__  
The data stored in memory can be of many types. For example, a person's name is a string, his age is a number, all the languages he knows is a list. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.  

Python has five standard data types −
* __Numbers__   
  There are four built-in data types for numbers:    
  * Normal integers like 123, 0
  * Floating-point numbers for numbers with decimal like 1.02, 314e-2
  * Long integers for numbers of huge size like 55000000000000000000L
  * Complex numbers like 3 + 4j
  
* __String__  
  Strings in Python are contiguous set of characters surrounded by either single quotes or double quotes, for e.g. `'python'`   or `"Java"`.Strings are zero indexed in python i.e. the first character is at zero index. A character of a string can be accessed by putting the index after the string name in square brackets, 
  ```
  str="Hello World"
  str[0] #returns H
  str[6] #returns W
  ```
  String are immutable and trying to change the value of a string will throw an error. Refer to [string manipulation](https://github.com/joed7/fose_python/blob/master/string-demo.py) for python source code.

* __List__  
  A list contains items separated by commas and enclosed within square brackets `lst=['Comp. Sc, Chemical Eng., Mech Eng']`. Lists are similar to arrays of programming languages like C, C++ or Java, but Python lists are by far more flexible than "classical" arrays. For example items in a list need not all have the same type. Furthermore a list size is not fixed and can grow in a program run, while in C the size of an array has to be fixed at compile time. Similar to strings, they are zero indexed and value of a item can be accessed in a similar manner.

    Refer to [list examples](https://github.com/joed7/fose_python/blob/master/list-demo.py) for python source code.

* __Tuple__  
  A tuple is an immutable list, i.e. the content of a tuple cannot be changed once it has been created. A tuple is defined similar to lists, except that the set of elements is enclosed in parentheses instead of square brackets. The rules for indices are the same as for lists. Sinces tuples are immutable, they can be used as keys in dictionaries, while lists can't.
  ```
  t = ('example','of','tuple')
  print t[0] #returns the first item of the tuple, 'example' in this case
  #t[0] = 'someValue' # Will throw an error
  ```
  
* __Dictionary__  
  Python's dictionaries store key-value pairs. A key in a dictionary is associated with a values and items are accessed via the keys they are associated with. While any data-type can be used as the value of dictionary, only immutable data-types can be used as keys i.e. list, dictionary can't be used a keys.  

  ```
  example_dict= {1:'one',2:'two',3:'three'} # dictionary storing numbers as keys and their string representation as values
  print example_dict[1] # returns value for key 1, throws a keys error if it does not exist
  print 2 in example_dict # checks if a key exists in dictionary
  ```
  Refer to [dictionary examples](https://github.com/joed7/fose_python/blob/master/dict-demo.py) for python source code.

[Previous](https://github.com/joed7/fose_python/blob/master/introduction.md)  |  [Home](https://github.com/joed7/Python)  |  [Next](https://github.com/joed7/fose_python/blob/master/syntax.md)
