#Python code synatx

__Indentation__  
Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced. The number of spaces in the indentation is four spaces or one tab. All statements within the block must be indented the same amount.

Here is a visualization for indentation:  
![](http://www.python-course.eu/images/blocks.png) 


__Conditonal statement__

Conditional statements are key in any programming langague. At various places, in our code, we have to check for certain conditions and proceed according to those conditions, For e.g. checking for the value of a variable, checking size of a list, checking if certain key exists etc.The simplest form is the if statement, which has the genaral form:  
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

