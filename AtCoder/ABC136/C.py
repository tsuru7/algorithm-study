def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

def main(n,h):
    hr=list(reversed(h))
    for i in range(n-1):
        if hr[i]<hr[i+1]:
            if hr[i+1]-hr[i]>1:
                return 'No'
            else:
                hr[i+1]-=1
    return 'Yes'

if __name__=='__main__':
    n,h=readinput()
    ans=main(n,h)
    print(ans)
