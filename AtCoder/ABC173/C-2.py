from copy import deepcopy

def readinput():
    h,w,k=list(map(int,input().split()))
    c=[]
    for _ in range(h):
        l=list(input())
        c.append(l)
    return h,w,k,c

def printC(c):
    for l in c:
        print(l)

def main(h,w,k,c):
    ans=0
    for g in range(2**h):
        for r in range(2**w):
            cc=deepcopy(c)
            for i in range(h):
                b=2**i
                if g & b == b:
                    for j in range(w):
                        cc[i][j]='*'
            for j in range(w):
                b=2**j
                if r & b == b:
                    for i in range(h):
                        cc[i][j]='*'
            #print(g,r)
            #printC(cc)
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
