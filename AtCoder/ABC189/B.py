def readinput():
    n,x=map(int,input().split())
    vp = []
    for _ in range(n):
        v, p =map(int,input().split())
        vp.append((v,p))
    return n,x,vp

def main(n,x,vp):
    sum=0
    for i in range(n):
        sum += vp[i][0] * vp[i][1]
        # print(i, sum, x)
        if sum > x*100:
            return i+1
    else:
        return -1 

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,vp=readinput()
    ans=main(n,x,vp)
    printans(ans)
