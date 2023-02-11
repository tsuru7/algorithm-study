import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    a=l_input()
    return n,a

def solve(n,a):
    residues = [0 for _ in range(100)]
    for i in range(n):
        ai = a[i]
        residues[ai % 100] += 1

    ans=0
    ans += residues[0]*(residues[0]-1)//2
    ans += residues[50]*(residues[50]-1)//2
    for i in range(1, 50):
        ans += residues[i]*residues[100-i]

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
