##Python and Modular programming

Modular development is one of the core components of software development. Modular programming technique says that rather than creating a big file doing a lot of things, the code should be split in separate parts, called modules, where each part has related code which works more or less independently. Modular development allows us to logically organize our Python code. 

A module is a file containing Python definitions and statements. The module name is the name of the file without the .py part. For example, if the file name is helper.py, the module name is helper.

For e.g. consider this function in the fibonacci.py script

```
map1={}
def fib(n):
    '''returns nth number in the fibonacci sequence 
    '''
    if n in map1:
        return map1[n]
    if n==0 or n ==1:
        map1[n]=n
        return n
    else:
        val=fib(n-1)+fib(n-2)
        map1[n]=val
        return val
```        
We can import this module in the python shell or in another python script using the statement `import fibonacci` and call the fib method `fibonacci.fib(10)`. While importing a module, the name of the namespace can be changed, for e.g. the above statements can be changed to `import fibonacci as fb` and `fb.fib(10)`.

Consider another scenario where we have a bunch of constants we have to use throughout our project. Rather than defining them in each file, we can create a module `proj-constants.py` and import the module in the file where we need the constants, via `import proj-constatnts` and `print proj-constatnts.conference`.

```
'''
Python script to define constants 
'''

conference = 'Conference'.lower()
division = 'Division'.lower()
founded = 'Founded'.lower()
arena = 'Home arena'.lower()
city = 'City'.lower()
manager = 'General manager'.lower()
coach = 'Head coach'.lower()
cups = 'Stanley Cups'.lower()

```

Python offer an array of in-built modules, some of the most useful ones are as follows:

* `math` : provides access mathematical  functions like sin, cos, factorial, ciel etc.
* `re`   : provides support for regular expressions
* `random`: generates pseudo-random numbers with various common distributions.
* `os`   : provides os routines across various operating systems 


Besides in-built modules, outside modules can be installed separately and imported.

In order to view help for a python module, `help('moduleName')` can be used in the python command shell, while the command `dir('moduleName')` displays the attributes and methods of a module.  

__Installing External Module Using Pip__

Pip is a tool for installing or managing Python packages. According to wikipaedia

`pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python"`

For installation instructions, refer to [pip documentation](https://pip.pypa.io/en/stable/installing/#install-pip).

[Previous](https://github.com/joed7/fose_python/blob/master/syntax.md)  |  [Home](https://github.com/joed7/Python/blob/master/home.md)  |  [Next](https://github.com/joed7/fose_python/blob/master/filemangement.md)

