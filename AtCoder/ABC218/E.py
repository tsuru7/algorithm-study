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
    n,m=m_input()
    edgeList = []
    loopList = []
    apex = [0]*n
    for _ in range(m):
        a,b,c = m_input()
        a -= 1
        b -= 1
        if a == b:
            loopList.append((c, a, b))
        else:
            edgeList.append((c, a, b))
        apex[a] += 1
        apex[b] += 1
    return n,edgeList,loopList,apex

def main(n,edgeList,loopList,apex):
    ans=0
    loopList.sort(reverse=True, key=lambda x: x[0])
    edgeList.sort(reverse=True, key=lambda x: x[0])
    for c, a, b in loopList:
        if c > 0:
            ans += c
        apex[a] -= 1
        apex[b] -= 1
    for c, a, b in edgeList:
        if c <= 0:
            break
        if apex[a] > 1 and apex[b] > 1:
            ans += c
            apex[a] -= 1
            apex[b] -= 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,edgeList,loopList,apex=readinput()
    ans=main(n,edgeList,loopList,apex)
    printans(ans)
