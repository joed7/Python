##Regular-Expressions

[Regular expressions](http://www.regular-expressions.info/tutorial.html) are text matching patterns. The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original. Expressions can include literal text matching, repetition, pattern-composition, branching, and other sophisticated rules. Regular expressions are typically used in applications that involve a lot of text processing. For example, they are commonly used as search patterns in text editing programs used by developers, including vi, emacs, and modern IDEs. They are also an integral part of Unix command line utilities such as sed, grep, and awk. Python's module for regular expression is `re`.

```
''' Python script to extract numbers from given text
'''

import re

pattern = r'[0-9]+'
text = ['The current sesaon is 2009-2010','Hello World']

for i  in text:
    match = re.search(pattern, i)

    if match != None:
        s = match.start()
        e = match.end()

        print 'Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, i[s:e])


```
Description of the functions and variable used in the code above

`search()` : takes the pattern and text to scan, and returns a Match object when the pattern is found. If the pattern is not found, search() returns None.

`match` : The Match object returned by `search()` holds information about the nature of the match, including the original input string, the regular expression used, and the location within the original string where the pattern occurs.

`start() and end()`: The start() and end() methods give the integer indexes into the string showing where the text matched by the pattern occurs.

The `re` module provides one more function `finditer()` which returns the match objects for all the substring matching the pattern.

```
'''Above script using finditer(), returns all of the number substrings
'''
import re

pattern = r'[0-9]+'
text = ['The current season is 2009-2010','Hello World']

for i  in text:
    for match in re.finditer(pattern,i):
        if match != None:
            s = match.start()
            e = match.end()

            print 'Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, i[s:e])


```

Another useful function `re` provides is `group()`.
`group()`: It allows us to access the matched substring by grouping parentheses, to get the matched substring of the n-th group, we call group() with the argument n: `group(n)`.

```
'''Python scrirpt demonstrating group()
'''
import re

pattern = r'([A-Z]+)[^0-9]*([0-9]+)'
text = ['BOULDER\'s pincode is 80304','DENVER\'s pincode is 80306']

for i  in text:
    match = re.search(pattern, i)
    if match != None:
        print "Pincode for the city "+ str(match.group(1))+" is "+str(match.group(2))

```        

Refer to the [regex-demo](https://github.com/joed7/Python/blob/master/python-regex.py) for python source code.

[Previous](https://github.com/joed7/fose_python/blob/master/filemangement.md)  |  [Home](https://github.com/joed7/Python/blob/master/home.md)  |  [Next](https://github.com/joed7/fose_python/blob/master/databases.md)
