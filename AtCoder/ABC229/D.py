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
    s = input()
    k=i_input()
    return s, k

def main(s, k):
    n = len(s)
    dotplaces = []
    for i in range(n):
        if s[i] == '.':
            dotplaces.append(i)
    if len(dotplaces) <= k:
        return n
    
    dotplaces.append(n)
    dotplaces.insert(0, -1)

    l = 1
    maxlen = 0
    while l+k < len(dotplaces):
        head = dotplaces[l-1]+1
        tail = dotplaces[l+k]-1
        if maxlen < tail-head+1:
            maxlen = tail-head+1
        l += 1
        
    return maxlen

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, k=readinput()
    ans=main(s, k)
    printans(ans)
