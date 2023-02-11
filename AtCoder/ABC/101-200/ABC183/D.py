def readinput():
    n,w=map(int,input().split())
    stp = []
    for _ in range(n):
        stp.append(list(map(int,input().split())))
    return n,w,stp

def main(n,w,stp):
    hist = [0]*(2*10**5+1)
    for s, t, p in stp:
        hist[s]+=p
        hist[t]-=p
    need=0
    for i in range(2*10**5+1):
        need+=hist[i]
        if need > w:
            return 'No'
    return 'Yes'

if __name__=='__main__':
    n,w,stp=readinput()
    ans=main(n,w,stp)
    print(ans)
