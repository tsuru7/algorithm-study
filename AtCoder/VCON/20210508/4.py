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
    na, nb=m_input()
    a=l_input()
    b=l_input()
    return na,nb,a,b

def main(na,nb,a,b):
    seta = set(a)
    setb = set(b)
    intersection_ab = seta.intersection(setb)
    union_ab = seta.union(setb)
    return len(intersection_ab)/len(union_ab)

def printans(ans):
    print(ans)

if __name__=='__main__':
    na,nb,a,b=readinput()
    ans=main(na,nb,a,b)
    printans(ans)
