import urllib
import re
import string

# Main module
def Main():
    papersListHtml = 'c:\\LibGraph\\list.txt'
    urlList = 'c:\\LibGraph\\urllist.txt'
    extractPapersUrl(papersListHtml, urlList)
    print 'Done.'


def extractPapersUrl(queryResultsFile, urlList): 
		
    f1 = open(queryResultsFile, "r")
    f2 = open(urlList, "w")
    pattern1 = re.compile("item.asp\?id=(\d+)") # define regular expression to find papers URLs		
    inputText = str(f1.readlines())              # convert input file into a big string	
    print inputText
    ids = pattern1.findall(inputText)            # find all matches 
    for line in ids:
        res = "http://elibrary.ru/item.asp?id=" + line + "\n"
        f2.write(res)
        # print res
    f1.close()
    f2.close()

Main() 