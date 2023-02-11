class Node:
    def __init__(self):
        self.parent=-1
        self.child=-1
        self.sibling=-1
        self.money=0
    
    def print(self):
        print([self.parent, self.child, self.sibling, self.money])
    
def printNodeList(nodeList):
    for node in nodeList:
        node.print()
    print('')

def readinput():
    n=int(input())
    nodeList=[Node()]
    for _ in range(n):
        nodeList.append(Node())
    for i in range(2,n+1):
        b=int(input())
        nodeList[i].parent=b
        current=i
        parent=b
        next=nodeList[b].child
        if next==-1:
            nodeList[b].child=i
            #printNodeList(nodeList)
        else:
            while next!=-1:
                current=next
                next=nodeList[current].sibling
            nodeList[current].sibling=i
            #printNodeList(nodeList)
    return n,nodeList

import sys
INFTY=sys.maxsize
def dfs(s,nodeList):
    if nodeList[s].child==-1:
        nodeList[s].money=1
    else:
        maxchild=0
        minchild=INFTY
        next=nodeList[s].child
        while(next!=-1):
            nextmoney=dfs(next,nodeList)
            maxchild=max(maxchild,nextmoney)
            minchild=min(minchild,nextmoney)
            next=nodeList[next].sibling
        nodeList[s].money=(maxchild+minchild)+1
    #printNodeList(nodeList)
    return nodeList[s].money 

def main(n,nodeList):
    ans=dfs(1,nodeList)
    return ans

if __name__=='__main__':
    n,nodeList=readinput()
    ans=main(n,nodeList)
    print(ans)




