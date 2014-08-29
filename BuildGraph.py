
# neato -Tpng -O orggraph.txt
def makeDot(inFileName = 'c:\\LibGraph\\orgdata.txt', resFileName = 'c:\\LibGraph\\orggraph.txt') :

    inFile = open(inFileName, 'r')
    outFile = open(resFileName, 'w')

    outFile.write('digraph G {\n')
    
    nodesInEdges = []
    allNodes = []
    edges = []

    for line in inFile.readlines() :
        data = line.strip().split('\t')
        if data[1] == 'Pairs:':
            size = len(data) - 2
            orgList = []
            for i in range(size) :
                pair = data[i+2]

                resLine = '    ' + pair
                resLine = resLine + ' [arrowhead = none, len=10];\n'
                outFile.write(resLine)

                nodesInEdges = nodesInEdges + pair.split(' -> ')
                orgList = orgList + pair.split(' -> ')
            allNodes = allNodes + list(set(orgList)) 
        elif data[1] == 'Single:' :
            allNodes = allNodes + [data[2]] 


    nodes = list(set(nodesInEdges))
    nodes = [[value, nodesInEdges.count(value), allNodes.count(value)] for value in nodes ]

    print '\n'.join(nodesInEdges), '\n', nodes

    for [node, number, quantity] in nodes :
        size = str(0.4 + (quantity - 1.0)/10.0)
        if size > 1.0 :
            size = str(1.0)
        if quantity > 1 :
            label = str(quantity)
        else :
            label = '""'
        resLine = str(node) + ' [width = ' + size + ', height = '+ size + ', fixedsize=true, '
        resLine = resLine + 'label = ' + label + ' ];\n'
        outFile.write(resLine)
    
    outFile.write('}\n')
    inFile.close()
    outFile.close()


