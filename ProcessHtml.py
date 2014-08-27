import re
import os
import time

def extractPaperUrlFromFolder(inFolder, resFolder = 'c:\\tmp\\try3\\'):

    timestamp = '' #time.asctime().replace(' ','_').replace(':','_')
    resFileName = os.path.join(resFolder, 'urllist_' + timestamp + '.txt')

    fileList = os.listdir(inFolder)
    for inFileName in fileList:
        fullInName = os.path.join(inFolder, inFileName)
        if not os.path.isdir(fullInName) :
            extractPaperUrl(fullInName, resFileName)

    return resFileName

def extractPaperUrl(queryHtmlFile, resFile = 'c:\\tmp\\urllist.txt'): 
		
    f1 = open(queryHtmlFile, "r")
    if os.path.exists(resFile) :
        f2 = open(resFile, "a")
    else :
        f2 = open(resFile, "w")
    pattern1 = re.compile("item.asp\?id=(\d+)") # define regular expression to find papers URLs		
    inputText = '  '.join(f1.readlines()).replace('\n','')
    lst =  pattern1.split(inputText)
    flag = 0
    for line in lst:
        if flag == 1 :
            res = "http://elibrary.ru/item.asp?id=" + line + '\t'
        else :
            
            res = line[7:len(line)] #remove first 7 symbols
            res = res.replace('</b></a><br><font color="#00008f"><i>  ','\t')
            res = res.replace('</i></font><br>  <font color="#00008f">  ','\t')
            res = res + '\n'
        print flag, res[0:50]
        f2.write(res )
        flag = 1-flag
     
    f1.close()
    f2.close()


def extractPaperData(inFileName):

    f = open(inFileName, "r")
    data = ' '.join(f1.readlines())
    f1.close()

    orgs = orgPattern.findall(data)
    orgs = list(set(orgs)) # remove dublicates
    size = len(orgs)

    if size == 0 :
        print 'NO ORGANIZATIONS FOUND'
        return ''
    elif size == 1:
        return ''
    elif size == 2 :
        return [orgs]
    else :
        res = []
        for i in range(size - 1) :
            for j in range (size - 1 - i) :
                res = res.append([orgs[i], orgs[j+i+1]])
        return res
    print 'Data extracted from', inFileName