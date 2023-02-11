import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    damages = [0 for _ in range(n)]
    damage = 0
    ans=0
    for i in range(n):
        x, h = monster[i]
        damage += damages[i]
        hp = h - damage
        # print(f'i: {i}, damage: {damage}, hp: {hp}')
        if hp <= 0:
            continue
        nbomb = hp // a
        if hp % a > 0:
            nbomb += 1
        right = x + 2*d
        damages[i] += nbomb*a
        damage += nbomb*a
        idx = bisect_left(monster, [right, INFTY])
        # 爆破範囲が右端のモンスターを含まないとき
        if idx < len(monster):
            damages[idx] -= nbomb*a
        ans += nbomb
        # print(f'damages: {damages}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,a,monster=readinput()
    ans=solve(n,d,a,monster)
    printans(ans)
