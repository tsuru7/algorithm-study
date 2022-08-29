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
    p=i_input()
    return p

def main(p):
    factnum = [0]*11
    factnum[1]=1
    for i in range(2, 11):
        factnum[i] = i*factnum[i-1]
    count = 0
    i = 10
    while p > 0 and i > 0:
        if p < factnum[i]:
            i -= 1
            continue
        p -= factnum[i]
        count += 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    p=readinput()
    ans=main(p)
    printans(ans)
