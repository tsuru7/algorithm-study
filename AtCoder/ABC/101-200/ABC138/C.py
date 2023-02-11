from heapq import heappush, heappop, heapify

def readinput():
    n=int(input())
    v=list(map(int,input().split()))
    return n,v

def main(n,v):
    heapify(v)
    while(len(v)>1):
        x=heappop(v)
        y=heappop(v)
        heappush(v,(x+y)/2)
    
    return v[0]

if __name__=='__main__':
    n,v=readinput()
    ans=main(n,v)
    print(ans)
