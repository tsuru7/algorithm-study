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
    n=i_input()
    st = []
    for _ in range(n):
        s, tstr = input().split()
        st.append([int(tstr), s])
    return n,st

def main(n,st):
    st.sort(reverse=True, key=lambda x: x[0])
    ans=st[1][1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,st=readinput()
    ans=main(n,st)
    printans(ans)
