
#Python syntax and datatypes

###__Python Variables__  

Variables are reserved memory locations to store values. This means that when we create a variable you reserve some space in memory. Depending on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.        
Values can be assigned to variables with equal sign `=`.  

  ```
  year=2015  #integer assignment
  month='august' #string assignment  
  salary=160.05 #float assignment
  ```
The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable

  __Data Type__  
The data stored in memory can be of many types. For example, a person's name is a string, his age is a number, all the languages he knows a lsitetc. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.  

Python has five standard data types −
* __Numbers__   
  There are four built-in data types for numbers:    
  * Normal integers like 123, 0
  * Floating-point numbers for numbers with decimal like 1.02, 314e-2
  * Long integers for numbers of huge size like 55000000000000000000L
  * Complex numbers like 3 + 4j
  
* __String__  
  Strings in Python are contiguous set of characters surrounded by either single quotes or double quotes, for e.g. `'python'`   or `"Java"`. Strings are zero indexed in python i.e. the first character is at zero index. A character of a string can be accessed by putting the index after the string name in square brackets, 
  ```
  str="Hello World"
  str[0] #returns H
  str[6] #returns W
  ```
  Refer to [string manipulation](https://github.com/joed7/fose_python/blob/master/string-demo.py) for python source code.

* __List__
* Tuple
* Dictionary
