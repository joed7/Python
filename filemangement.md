##File Manipulation in Python

Python offers a very simple and intuitive interface for File I/O. Python provides a function open `open('filename','flag')` which returns a file object which can be used to read/write a file. Some examples

* `fobj = open('names.txt')` --omitting the flag opens the file in read-only mode
* `fobj = open('output.txt','w')` -- returns the file object which can be used for writing into the file, creates the file if not already exists

Upon getting file object, it can be used for reading or writing. Some common functions that are used to accomplish these tasks are

* `fobj.read()` -- read the content of the whole file in a string
* `fobj.readlines()` -- read the content of the whole file in a list with each item representing a line of text
* `fobj.write('text')` -- write the context text to the file.

Source-code for File I/O can be found [here](https://github.com/joed7/fose_python/blob/master/wordcount.py). The python script reads the text of a file, computes the number of words, lines, characters in the text and saves it in a output file.

[Previous](https://github.com/joed7/fose_python/blob/master/modules.md)  |  [Home](https://github.com/joed7/Python/blob/master/home.md)  |  [Next](https://github.com/joed7/Python/blob/master/text-processing.md)
