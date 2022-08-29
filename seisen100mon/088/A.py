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
    n=i_input()
    cList = [i_input() for _ in range(n)]
    return n,cList

def solve(n,cList):
    stone = [[cList[0], 1]]
    for i in range(1, n):
        ci = cList[i]
        if i % 2 == 0:
            if stone[-1][0] == ci:
                stone[-1][1] += 1
            else:
                stone.append([ci, 1])
        else:
            if stone[-1][0] == ci:
                stone[-1][1] += 1
            else:
                cj, nj = stone.pop()
                if len(stone) == 0:
                    stone.append([ci, nj+1])
                else:
                    stone[-1][1] += nj+1
    ans=0
    # print(f'stone: {stone}')
    for c, n in stone:
        if c == 0:
            ans += n
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,cList=readinput()
    ans=solve(n,cList)
    printans(ans)
