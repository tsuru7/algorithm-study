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
    n,a,b=m_input()
    p,q,r,s=m_input()
    return n,a,b,p,q,r,s

def main(n,a,b,p,q,r,s):
    ans = []
    offset_i = p
    offset_j = r
    for i in range(q-p+1):
        line = ['.']*(s-r+1)
        for j in range(s-r+1):
            original_i = i + offset_i
            original_j = j + offset_j
            if original_i - original_j == a-b or original_i + original_j == a+b:
                line[j] = '#'
        ans.append(''.join(line))
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a,b,p,q,r,s=readinput()
    ans=main(n,a,b,p,q,r,s)
    printans(ans)
