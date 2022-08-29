import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import combinations

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
    xy = [ l_input() for _ in range(n) ]
    return n,k,xy

def solve(n,k,xy):
    if k == 1:
        return 'Infinity'
    ans=0
    checked = set()
    for i in range(n):
        xi, yi = xy[i]
        for j in range(i+1, n):
            xj, yj = xy[j]
            if (i, j) in checked:
                continue
            points = [i, j]

            for l in range(j+1, n):
                xl, yl = xy[l]
                if (xl-xi)*(yj-yi)-(xj-xi)*(yl-yi) == 0:
                    points += [l]
            if len(points) >= k:
                ans += 1
                for c in combinations(points, 2):
                    checked.add(c)
            # print(f'i: {i}, j: {j}, points: {points}, checked: {checked}')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,xy=readinput()
    ans=solve(n,k,xy)
    printans(ans)
