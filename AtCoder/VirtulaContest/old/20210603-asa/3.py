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
    n,k=m_input()
    r, s, p = m_input()
    t=input()
    return n,k,r,s,p,t

def main(n,k,r,s,p,t):
    history = []
    ans=0
    for i in range(k):
        if t[i] == 'r':
            ans += p
            history.append('p')
        elif t[i] == 's':
            ans += r
            history.append('r')
        elif t[i] == 'p':
            ans += s
            history.append('s')
    for i in range(k, n):
        # print(f'i: {i}, k: {k}, n: {n}, history: {history}')
        if t[i] == 'r':
            if history[i-k] != 'p':
                ans += p
            history.append('p')
        elif t[i] == 's':
            if history[i-k] != 'r':
                ans += r
            history.append('r')
        elif t[i] == 'p':
            if history[i-k] != 's':
                ans += s
            history.append('s')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,r,s,p,t=readinput()
    ans=main(n,k,r,s,p,t)
    printans(ans)
