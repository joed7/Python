'''python scipt to demonstrate File I/O in python. 
Compute word count, equivalent to wc  in shell.
wc text
68  651 3898 text
'''
inputFile = 'text'
outputFile = 'output'

def wordCount():
    '''Computes the wordcount for the specified input file
    '''
    lines = 0
    words = 0
    characters = 0
    
    fobj = open(inputFile)
    #calculation to compute total number of lines
    textInList = fobj.readlines()
    lines = len(textInList)
    
    #calculation to compute total number of words
    wordList=[]
    for i in textInList:
        textInLines = i.split()
        for word in textInLines:
            if len(word) > 0:
                wordList.append(word)
                
    words = len(wordList)
    
    #calculation to compute total number of character
    c=0
    for i in textInList:
        c = c +len(i)
    characters =c
    output = "wc "+inputFile +"\n"+str(lines) + ' '+str(words)+' '+str(characters)+ ' '+  inputFile 
    print output    
    fobj.close()
    save(output)
    
    
def save(outputText):
    '''saves outputText in the specified outputfile
    '''
    fobj = open(outputFile,'w')
    fobj.write(outputText+"\n")
    fobj.close()

wordCount()    
