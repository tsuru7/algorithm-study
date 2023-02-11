def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

def main(n,h):
    maxstep=0
    step=0
    for i in range(n-1):
        if h[i]>=h[i+1]:
            step+=1
        else:
            maxstep=max(maxstep,step)
            step=0
    else:
        maxstep=max(maxstep,step)
    return maxstep

if __name__=='__main__':
    n,h=readinput()
    ans=main(n,h)
    print(ans)
