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
    a,b=m_input()
    p=l_input()
    q=l_input()
    return a,b,p,q

def main(a,b,p,q):
    ans = ['x']*10
    for x in p:
        x -= 1
        ans[x] = '.'
    for x in q:
        x -= 1
        ans[x] = 'o'

    ans1 = []
    left = 0
    right = 0
    for i in range(4):
        ans1.append(ans[left:right+1])
        left = right+1
        right = left + i+1
    ans2 = []
    for i in range(4)[::-1]:
        ans2.append(' '*(3-i)+' '.join(map(str,ans1[i])))
    return ans2

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    a,b,p,q=readinput()
    ans=main(a,b,p,q)
    printans(ans)
