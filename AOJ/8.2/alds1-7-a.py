class Node:
    def __init__(self, id=0):
        self.id=id
        self.child=[]
        self.parent=-1
        self.depth=0
        self.type=''

def readinput():
    n=int(input())
    nodeList = []
    for _ in range(n):
        node=Node(id=_)
        nodeList.append(node)
    #printNodeList(nodeList)
    for _ in range(n):
        l=list(map(int,input().split()))
        node=nodeList[l[0]]
        node.child=l[2:]
        node.parent=-1
        node.depth=0
        node.type=''
        #nodeList[node.id]=node
    #printNodeList(nodeList)

    return nodeList

def setParent(nodeList):
    for i, node in enumerate(nodeList):
        for c in node.child:
            nodeList[c].parent=i
    return

def findRoot(nodeList):
    root=-1
    for i in range(len(nodeList)):
        if(nodeList[i].parent==-1):
            root=i
            break
    return root

def setDepth(nodeList, parent, depth):
    #print('[setDepth] parent: {}, child:{}, depth: {}'.format(parent, nodeList[parent].child, depth))
    pNode=nodeList[parent]
    pNode.depth=depth
    ch=pNode.child
    if(len(ch)==0):
        pNode.type='leaf'
        return
    pNode.type='internal node'
    for c in ch:
        setDepth(nodeList, c, depth+1)

def printNodeList(nodeList):
    for node in nodeList:
        print('id: {}, child: {}, parent: {}, depth: {}, type: {}'.format(node.id, node.child, node.parent, node.depth, node.type))

def main(nodeList):
    setParent(nodeList)
    #printNodeList(nodeList)
    root=findRoot(nodeList)
    setDepth(nodeList, root, 0)
    nodeList[root].type='root'

    for i, node in enumerate(nodeList):
        print('node {}: parent = {}, depth = {}, {}, {}'.format(node.id, node.parent, node.depth, node.type, node.child))
    return    

if __name__=='__main__':
    nodeList=readinput()
    main(nodeList)

