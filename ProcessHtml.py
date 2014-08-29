import re
import os
import time
import random

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


def extractPublicationDataFromFolder(folderName = 'c:\\LibGraph\\Blocks1317\\', resFileName = 'c:\\LibGraph\\orgdata.txt'):

    resFile = open(resFileName,'w')

    fileList = os.listdir(folderName)
    for fileName in fileList :
        [orgList, resTxt] = extractPublicationData(os.path.join(folderName, fileName))
        resFile.write(resTxt)

    resFile.close()

def extractPublicationData(inFileName):
    print '\nExtracting from', inFileName
    f = open(inFileName, "r")
    data = ' '.join(f.readlines())
    f.close()

    orgPattern = re.compile("orgsid=(\d+)")
    orgs = orgPattern.findall(data)
    orgs = list(set(orgs)) # remove dublicates
    size = len(orgs)

    if size == 0 :
        resTxt = 'NO ORGANIZATIONS FOUND'
        resList = []
    elif size == 1:
        resTxt = 'Single:\t' + str(orgs[0])
        resList = orgs[0]
    elif size == 2 :
        resTxt = 'Pairs:\t' + str(orgs[0]) + ' -> ' + str(orgs[1])
        resList = [orgs]
    else :
        resTxt = 'Pairs:'
        resList = []
        for i in range(size - 1) :
            for j in range (size - 1 - i) :
                print resList, '- appending', i, j+i+1, str([orgs[i], orgs[j+i+1]])
                pair = [orgs[i], orgs[j+i+1]]
                resTxt = resTxt + '\t' + str(pair[0]) + ' -> ' + str(pair[1])
                if len(resList) == 0 :
                    resList = [pair]
                else :
                    resList = resList + [pair]
    resTxt = inFileName + '\t' + resTxt + '\n'
    print resTxt
    print 'Data extracted from', inFileName, resList
    return [resList, resTxt]


def splitFile():
    inFileName = 'c:\\LibGraph\\urllist_0.txt'
    f_in = open(inFileName,'r')
    dataList = f_in.readlines()
    random.shuffle(dataList)
    k = 230
    i = 0
    n = 0
    f_out = open('c:\\LibGraph\\blocks\\utrlist_block_' + str(n) +'.txt', 'w')
    for line in dataList :
        f_out.write(line)
        i += 1
        if i == k :
            i = 0
            n += 1
            f_out.close()
            f_out = open('c:\\LibGraph\\blocks\\utrlist_block_' + str(n) +'.txt', 'w')


