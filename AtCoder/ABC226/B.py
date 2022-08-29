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
    lset = set()
    for _ in range(n):
        l=l_input()
        l = l[1:]
        lset.add(' '.join(map(str,l)))
    return len(lset)

def main(answer):
    ans=answer
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    answer=readinput()
    ans=main(answer)
    printans(ans)
