def readinput():
    l=list(map(int,input().split()))
    return l

def main(l):
    for i in range(5):
        if l[i]==0:
            return i+1

if __name__=='__main__':
    l=readinput()
    ans=main(l)
    print(ans)
