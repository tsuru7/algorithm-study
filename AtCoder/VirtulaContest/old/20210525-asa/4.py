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
    p=l_input()
    return n,p

def main(n,p):
    ans = []
    p.insert(0,0)
    head = 1
    while head < n:
        # find
        for i in range(head, n+1):
            if p[i] == head:
                tail = i
                break
        # print(f'head: {head}, tail: {tail}')
        if head == tail:
            return [-1]
        # replace
        for i in range(tail-1, head-1, -1):
            p[i], p[i+1] = p[i+1], p[i]
            ans.append(i)
        # print(f'p: {p}')
        # check
        for i in range(head, tail):
            if p[i] != i:
                return [-1]
        # print('ok')
        head = tail
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
