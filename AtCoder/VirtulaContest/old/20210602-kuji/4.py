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
    n,m=m_input()
    slist = []
    for _ in range(m):
        l = l_input()
        slist.append(l[1:])
    p=l_input()
    return n,m,slist,p

def main(n,m,slist,p):
    ans=0
    for i in range(2**n):
        switch = [0]*(n+1)
        b = 1
        for j in range(n):
            if i & b == b:
                switch[j+1] = 1
            b *= 2
        # print(f'i: {i}, switch: {switch[1:]}')

        light = True
        for s, parity in zip(slist, p):
            n_on = 0
            for t in s:
                n_on += switch[t]
            if n_on % 2 != parity:
                light = False
            # print(f's: {s}, parity: {parity}')
        if light:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,slist,p=readinput()
    ans=main(n,m,slist,p)
    printans(ans)
