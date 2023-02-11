import heapq

def readinput():
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,m,a

def main(n,m,a):
    #print(a)
    hq=[]
    for i in a:
        heapq.heappush(hq,-i)
    #print(hq)
    for i in range(m):
        a=(-heapq.heappop(hq))//2
        heapq.heappush(hq,-a)
        #print(hq)

    sum=0
    for i in hq:
        sum+=i
    
    return -sum

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)
