def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,k,s=m_input()
    return n,k,s

def main(n,k,s):
    a = []
    for i in range(k):
        a.append(s)
    if s < 10**9:
        for i in range(n-k):
            a.append(s+1)
    else:
        for i in range(n-k):
            a.append(s-1)
    return a

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n,k,s=readinput()
    ans=main(n,k,s)
    printans(ans)
