import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque
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
    s = input()
    return s

def main(s):
    MOD = 10**9+7

    C = 0
    H = 1
    O = 2
    K = 3
    U = 4
    D = 5
    A = 6
    I = 7
    n = len(s)
    pos = []
    for j in range(8):
        pos.append(deque())
    for i in range(n):
        c = s[i]
        if c == 'c':
            pos[C].append(i)
        elif c == 'h':
            pos[H].append(i)
        elif c == 'o':
            pos[O].append(i)
        elif c == 'k':
            pos[K].append(i)
        elif c == 'u':
            pos[U].append(i)
        elif c == 'd':
            pos[D].append(i)
        elif c == 'a':
            pos[A].append(i)
        elif c == 'i':
            pos[I].append(i)

    print(pos)

    ic = 0
    ih = 0
    io = 0
    ik = 0
    iu = 0
    id = 0
    ia = 0
    ii = 0

    ans=0
    
    while len(pos[C]) > 0:
        temp = 1
        ic = pos[C].popleft()

        while len(pos[H]) > 0 and pos[H][0] < ic:
            pos[H].popleft()
        if len(pos[H]) == 0:
            continue
        temp *= len(pos[H])
        temp = temp % MOD
        ih = pos[H][0]

        while len(pos[O]) > 0 and pos[O][0] < ih:
            pos[O].popleft()
        if len(pos[O]) == 0:
            continue
        temp *= len(pos[O])
        temp = temp % MOD
        io = pos[O][0]

        while len(pos[K]) > 0 and pos[K][0] < io:
            pos[K].popleft()
        if len(pos[K]) == 0:
            continue
        temp *= len(pos[K])
        temp = temp % MOD
        ik = pos[K][0]

        while len(pos[U]) > 0 and pos[U][0] < ik:
            pos[U].popleft()
        if len(pos[U]) == 0:
            continue
        temp *= len(pos[U])
        temp = temp % MOD
        iu = pos[U][0]

        while len(pos[D]) > 0 and pos[D][0] < iu:
            pos[D].popleft()
        if len(pos[D]) == 0:
            continue
        temp *= len(pos[D])
        temp = temp % MOD
        id = pos[D][0]

        while len(pos[A]) > 0 and pos[A][0] < id:
            pos[A].popleft()
        if len(pos[A]) == 0:
            continue

        temp *= len(pos[A])
        temp = temp % MOD
        iA = pos[A][0]

        while len(pos[I]) > 0 and pos[I][0] < ia:
            pos[I].popleft()
        if len(pos[I]) == 0:
            continue

        temp *= len(pos[I])
        temp = temp % MOD

        ans = (ans + temp) % MOD

        print(temp)
        print(pos)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
