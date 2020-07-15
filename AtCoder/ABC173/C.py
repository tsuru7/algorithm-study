from itertools import combinations
from copy import deepcopy

def readinput():
    h,w,k=list(map(int,input().split()))
    c=[]
    for _ in range(h):
        l=list(input())
        c.append(l)
    return h,w,k,c

def main(h,w,k,c):
    gyo=[]
    for i in range(1,h+1):
        for cmb in combinations(range(1,h+1),i):
            gyo.append(cmb)
    gyo.append(())

    retsu=[]
    for i in range(1,w+1):
        for cmb in combinations(range(1,w+1),i):
            retsu.append(cmb)
    retsu.append(())

    ans=0
    for g in gyo:
        for r in retsu:
            cc=deepcopy(c)
            #print(cc)
            #print(g,r)
            
            for i in g:
                for j in range(1,w+1):
                    cc[i-1][j-1]='*'

            for j in r:
                for i in range(1,h+1):
                    cc[i-1][j-1]='*'
            #print(cc)
            count=0
            for i in range(1,h+1):
                for j in range(1,w+1):
                    if cc[i-1][j-1]=='#':
                        count+=1
            if count==k:
                ans+=1

    return ans

if __name__=='__main__':
    h,w,k,c=readinput()
    ans=main(h,w,k,c)
    print(ans)
