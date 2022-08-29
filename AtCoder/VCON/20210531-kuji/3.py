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
    s = input()
    q = i_input()
    tablist = []
    for _ in range(q):
        tablist.append(l_input())
    return n,s,q,tablist

def main(n,s,q,tablist):
    flip = False
    s = list(s)
    for t, a, b in tablist:
        if t == 1:
            a -= 1
            b -= 1
            if flip:
                a = (a+n) % (2*n)
                b = (b+n) % (2*n)
            s[a], s[b] = s[b], s[a]
            # print(f'a: {a}, b: {b}, s: {s}')
        elif t == 2:
            flip = not flip
    ans = ''.join(s)
    if flip:
        ans = ans[n:] + ans[:n]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,q,tablist=readinput()
    ans=main(n,s,q,tablist)
    printans(ans)
