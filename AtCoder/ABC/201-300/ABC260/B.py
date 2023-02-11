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
    n,x,y,z=m_input()
    a=l_input()
    b=l_input()
    return n,x,y,z,a,b

def solve(n,x,y,z,a,b):
    students = []
    for i in range(n):
        students.append((-i, a[i], b[i], a[i]+b[i]))
    students.sort(reverse=True, key=lambda x: (x[1], x[0]))
    passed = students[:x]
    notpassed = students[x:]
    notpassed.sort(reverse=True, key=lambda x: (x[2], x[0]))
    passed += notpassed[:y]
    notpassed = notpassed[y:]
    notpassed.sort(reverse=True, key=lambda x: (x[3], x[0]))
    passed += notpassed[:z]
    passed.sort(reverse=True)
    return passed

def printans(ans):
    for a in ans:
        print(-a[0]+1)

if __name__=='__main__':
    n,x,y,z,a,b=readinput()
    ans=solve(n,x,y,z,a,b)
    printans(ans)
