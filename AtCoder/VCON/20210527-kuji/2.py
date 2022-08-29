import sys
sys.setrecursionlimit(10**5)
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
    n,m,t=m_input()
    ab = []
    for _ in range(m):
        a, b = m_input()
        ab.append((a,b))
    return n,m,t,ab

def main(n,m,t,ab):
    battery = n
    time = 0
    preb = 0
    for a, b in ab:
        battery -= (a - preb)
        if battery <= 0:
            return 'No'
        battery += (b-a)
        battery = min(battery, n)
        preb = b
    battery -= (t-preb)
    if battery <= 0:
        return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,t,ab=readinput()
    ans=main(n,m,t,ab)
    printans(ans)
