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

def main(n,k,s):
    updown = []
    down = True
    count = 0
    for i in range(n):
        c = s[i]
        if down and c == '1':
            count += 1
        elif down and c == '0':
            updown.append(count)
            down = not down
            count = 1
        elif not down and c == '0':
            count += 1
        elif not down and c == '1':
            updown.append(count)
            down = not down
            count = 1
    updown.append(count)

    l = 0
    if len(updown) // 2 <= k:
        return n
    if len(updown) % 2 == 0:
        updown.append(0)

    r = 2*k
    maxdown = 0
    for i in range(r+1):
        maxdown += updown[i]
    down = maxdown
    while r+2 < len(updown):
        down -= updown[l]
        down -= updown[l+1]
        down += updown[r+1]
        down += updown[r+2]
        maxdown = max(maxdown, down)
        l += 2
        r += 2

    return maxdown

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=main(n,k,s)
    printans(ans)
