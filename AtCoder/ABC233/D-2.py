import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n,k=m_input()
    a=l_input()
    return n,k,a

def main(n,k,a):
    cumsum = [0]*n
    cumsum[0] = a[0]
    for i in range(1, n):
        cumsum[i] = cumsum[i-1] + a[i]
    
    count = dict()
    for i in range(n):
        if cumsum[i] not in count:
            count[cumsum[i]] = 1
        else:
            count[cumsum[i]] += 1
    ans = 0
    lsum = 0
    for l in range(n):
        if lsum+k in count:
            ans += count[lsum+k]
        lsum = cumsum[l]
        count[lsum] -= 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
