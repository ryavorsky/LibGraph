import random

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



