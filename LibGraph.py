import ProcessHtml
import BuildGraph

inHtmlFolder = 'c:\\LibGraph\\genom2012\\'
urlListFolder = 'c:\\LibGraph\\'
papersListHtml = 'c:\\LibGraph\\list.txt'
urlList = 'c:\\LibGraph\\urllist.txt'

# Main module
def Main():
    BuildGraph.makeDot('c:\\LibGraph\\orgdata.txt')
    #ProcessHtml.extractPublicationDataFromFolder('c:\\LibGraph\\Blocks1317\\')
    print 'Done.'


Main() 