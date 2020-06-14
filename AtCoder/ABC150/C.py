from itertools import permutations

def readinput():
    n=int(input())
    P=tuple(map(int,input().split()))
    Q=tuple(map(int,input().split()))
    return n,P,Q

def main(n,P,Q):
    permlist=permutations(range(1,n+1))
    sortedList=sorted(permlist)
    #print(sortedList)
    np=sortedList.index(P)
    nq=sortedList.index(Q)
    return abs(np-nq)

if __name__=='__main__':
    n,P,Q=readinput()
    ans=main(n,P,Q)
    print(ans)
