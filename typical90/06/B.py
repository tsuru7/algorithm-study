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
    n,k=m_input()
    s=input()
    return n,k,s

def solve(n,k,s):
    cindex = [[INFTY for _ in range(n)] for _ in range(26)] # ループの長い方を後ろにする
    t = ''
    for i in range(n)[::-1]:
        si = ord(s[i]) - ord('a')
        cindex[si][i] = i
        if i < n-1:
            for ch in range(26):
                if ch == si:
                    continue
                cindex[ch][i] = cindex[ch][i+1]
    
    # print(*cindex, sep='\n')

    i = 0
    while i < n:
        # print(f'i: {i}')
        l = k-len(t)
        for ch in range(26):
            if cindex[ch][i] <= n-l:
                t += chr(ord('a')+ch)
                if len(t) == k:
                    return t
                i = cindex[ch][i]+1
                break

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=solve(n,k,s)
    printans(ans)
