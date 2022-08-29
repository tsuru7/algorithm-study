import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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
    n,d,a=m_input()
    monster = [l_input() for _ in range(n)]
    return n,d,a,monster

def solve(n,d,a,monster):
    monster.sort()
    count = 0
    damagehist = []
    damage = 0
    for i in range(n):
        x, h = monster[i]
        
        while len(damagehist) > 0 and damagehist[0][0] < x:
            _, dame = heappop(damagehist)
            damage += dame
        
        hp = h - damage
        if hp <= 0:
            continue
        bomb = hp//a
        if hp % a > 0:
            bomb += 1
        damage += bomb * a
        heappush(damagehist, (x+2*d, -bomb*a))
        count += bomb

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,a,monster=readinput()
    ans=solve(n,d,a,monster)
    printans(ans)
