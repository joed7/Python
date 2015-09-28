#Python code syntax

__Indentation__  
Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced. The number of spaces in the indentation is four spaces or one tab. All statements within the block must be indented the same amount.

Here is a visualization for indentation:  
![](http://www.python-course.eu/images/blocks.png) 


__Conditonal statement__

Conditional statements are key in any programming langague. At various places, in our code, we have to check for certain conditions and proceed according to those conditions, For e.g. checking for the value of a variable, checking size of a list, checking if certain key exists in the dictionary etc.The simplest form is the if statement, which has the genaral form:  
```
if BOOLEAN EXPRESSION:
    STATEMENTS
```
Some key points regarding the above psuedo-code of if statement:
* Colon(:) separates the header of the compound statement from the body.
* The line after the colon must be indented. 
* All lines indented the same amount after the colon will be executed whenever the BOOLEAN_EXPRESSION is true.

Here is an example of `if-else` block:
```
#Here isWeatherNice is a boolean variable, if its value is true 'Weather is nice' will be printed
if isWeatherNice == True:
    print('Weather is nice')
    
#Here we checking the value of the variable val and printing the appropriate message    
if val == 0:
    print('Value is zero!')
else:
    print("Value is non zero!")
```    

__Loops__  
Generally, statements are executed sequentially, However, loops allow us to execute statements in a repeated manners subject to certain conditions. Here is a flow chart illustrating the loop work-flow

![](http://www.python-course.eu/images/while_loop_1.png)

Python has two constructs for loops:
* While loop  
```
#Example of a while loop printing the statment 10 times.
i=0
while i < 10:
    print("This is the "+str(i+1)+" iteration" )
    i=i+1
```    
In the example above, we initialize a variable to zero, then we check the loop condition(whether it is less than 10); If it is, we execute and the print statment and increment it by one and check the condition again. When condition does not hold true, it comes out of the loop.

* For loop  
  Python uses iterator based construct for `for` loop. It steps through the items in any ordered sequence list, i.e. string, lists, tuples, the keys of dictionaries and other iterables. The python sytax for `for` loop looks like this
```
for <variable> in <sequence>:
	<statements>
```  	
  The items of the sequence object are assigned one after the other to the loop variable;And for each item the loop body is executed.  

```
#Example of for loop in python
fibonacci = [0,1,1,2,3,5,8,13,21]
for i in fibonacci:
    print i

```

__Functions__  
A function is a block of organized, reusable code which perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing. Python provides a number of in-built functions like print and len, and we can create functions of our own.

Syntax for function declaration looks like this  
```
def functionname( parameters ):
   "function_docstring"
   statements
   return [expression]
```   
Function definition begins with the keyword `def` followed by functionname and a optional parameter list separated by commas. Inside the function body, we write python statments followed by a option return statement.

```
def fac(n):
    ''' function to computer factorial of a given number
    '''
    if n < 0:
        return -1
    if n==0 or n ==1:
        return 1   
        
    f=1
    for i in range(n):
        f=f*(i+1)
    return f
```    
Above is a example of a fuction which computes factorial. It expects one parameter as argument the number n, it does the computation and returns the computed value. 
