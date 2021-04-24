def readinput():
    n,k=map(int,input().split())
    return n,k

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

def g2(x):
    return int(''.join(sorted(str(x))))

def main(n,k):
    a = n
    for i in range(k):
        a = g1(a) - g2(a)
    return a

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
