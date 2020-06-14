from itertools import permutations
from math import sqrt

def readinput():
    n=int(input())
    xyList=[]
    for _ in range(n):
        x,y=list(map(int,input().split()))
        xyList.append((x,y))
    return n,xyList

def main(n,xyList):
    sum=0.0
    factn=0
    for tup in permutations(range(n)):
        #print(tup)
        factn+=1
        x0=xyList[tup[0]][0]
        y0=xyList[tup[0]][1]
        for i in tup:
            x=xyList[i][0]
            y=xyList[i][1]
            sum+=sqrt((x-x0)**2+(y-y0)**2)
            x0=x
            y0=y
    ans=sum/factn
    return ans

if __name__=='__main__':
    n,xyList=readinput()
    #print(xyList)
    ans=main(n,xyList)
    print(ans)

