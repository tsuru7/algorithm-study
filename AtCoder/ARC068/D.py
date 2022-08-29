import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    dist = [0]*(10**5+1)
    multi = 0
    for v in a:
        dist[v] += 1
        if dist[v] > 1:
            multi += 1
    if multi %2 == 0:
        return n - multi
    else:
        return n - multi - 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
