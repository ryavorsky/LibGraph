import ProcessHtml

inHtmlFolder = 'c:\\LibGraph\\genom2012\\'
urlListFolder = 'c:\\LibGraph\\'
papersListHtml = 'c:\\LibGraph\\list.txt'
urlList = 'c:\\LibGraph\\urllist.txt'

# Main module
def Main():
    ProcessHtml.extractPaperUrlFromFolder(inHtmlFolder, urlListFolder)
    print 'Done.'


Main() 