#Extracting data from the web using Python

Python is often used to scrape data on the web. Consider a wikipedia page with a bunch of html tables in various categories. Extracting the data using regular expressions in shell, perl can be extremely difficult, However, python makes it a lot of easier through modules like [__requests__](http://docs.python-requests.org/en/latest/) and [__Beautiful Soup__](http://www.crummy.com/software/BeautifulSoup/).

__Requests Module__

Requests is an Apache2 Licensed HTTP library, written in Python, for making HTTP requests through python source code.
Most existing Python modules for sending HTTP requests are extremely verbose and cumbersome. Python's provides a in-built module urllib2 which provides HTTP capabilities but its api is thoroughly broken. It requires an enormous amount of work (even method overrides) to perform the simplest of tasks.

Example:
```
import requests
#make the http get request and store the response in r
r = requests.get('https://en.wikipedia.org/wiki/National_Hockey_League') 

#print the status code
print r.status_code

#print the headers
print r.headers

#print the resulting html
print r.text

```
Requests allow you to send HTTP/1.1 requests. You can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way. 

__Beautiful Soup__

Beautiful Soup uses a pluggable XML or HTML parser to parse a document into a tree representation. Beautiful Soup provides a few simple methods and Pythonic idioms for navigating,
searching, and modifying a parse tree: a toolkit for dissecting a document and
extracting what you need.


Refer to [Scraping Example](https://github.com/joed7/fose_python/blob/master/scraping.py) for an example of the modules above.

[Previous](https://github.com/joed7/fose_python/blob/master/numpy.md)  |  [Home](https://github.com/joed7/Python/blob/master/home.md)  |  [Next](https://github.com/joed7/fose_python/blob/master/code-example.md)
