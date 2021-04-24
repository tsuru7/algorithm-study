def readinput():
    v,t,s,d=map(int,input().split())
    return v,t,s,d

def main(v,t,s,d):
    if d < v*t or v*s < d:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    v,t,s,d=readinput()
    ans=main(v,t,s,d)
    printans(ans)
