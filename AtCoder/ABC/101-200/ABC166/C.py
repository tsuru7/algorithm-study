from heapq import heappush, heappop
def readinput():
    n,m=map(int,input().split())
    h=list(map(int,input().split()))
    nList=[]
    for i in range(n+1):
        nList.append([])
    for i in range(m):
        a,b=map(int,input().split())
        heappush(nList[a],-h[b-1])
        heappush(nList[b],-h[a-1])

    return n,m,h,nList

def main(n,m,h,nList):
    count=0
    for i in range(1,n+1):
        if len(nList[i])==0:
            count+=1
        else:
            hi=-heappop(nList[i])
            if h[i-1]>hi:
                count+=1
    return count

if __name__=='__main__':
    n,m,h,nList=readinput()
    ans=main(n,m,h,nList)
    print(ans)
