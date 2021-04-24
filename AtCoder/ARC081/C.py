from heapq import heappop, heapify

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    for i in range(n):
        a[i] = -a[i]
    heapify(a)
    e1 = heappop(a)
    e2 = heappop(a)
    while e1 != e2 and len(a) > 0:
        e1 = e2
        e2 = heappop(a)
    else:
        if e1 != e2:
            return 0
    if len(a) < 2:
        return 0
    e3 = heappop(a)
    e4 = heappop(a)
    while e3 != e4 and len(a) > 0:
        e3 = e4
        e4 = heappop(a)
    else:
        if e3 != e4:
            return 0
    return e1 * e3

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
