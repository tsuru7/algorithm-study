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
    a.insert(0, 0)
    dist = {}
    count = 0
    for i in range(2, n+1):
        if (i-1)+a[i-1] in dist:
            dist[(i-1)+a[i-1]] += 1
        else:
            dist[(i-1)+a[i-1]] = 1
        if (i-a[i]) in dist:
            count += dist[i-a[i]]
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
