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
    n=i_input()
    s = input()
    return n,s

def solve(n,s):
    head = Node()
    tail = Node()
    zero = Node(0)
    head.right = zero
    tail.left = zero
    zero.left = head
    zero.right = tail
    now = zero
    for i in range(n):
        c = s[i]
        newnode = Node(i+1)
        if c == 'L':
            leftnode = now.left
            leftnode.right = newnode
            newnode.left = leftnode
            newnode.right = now
            now.left = newnode
        else:
            rightnode = now.right
            rightnode.left = newnode
            newnode.right = rightnode
            newnode.left = now
            now.right = newnode
        now = newnode
    ans = []
    now = head
    while now.right != None:
        now = now.right
        ans.append(now.data)


    return ans[:-1]

def printans(ans):
    print(*ans)

class Node:
    def __init__(self, data=-1):
        self.data = data
        self.left = None
        self.right = None

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
