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
    return s,k

def main(s,k):
    ans=[]
    for c in s:
        if c == 'a':
            ans.append('a')
            continue
        if ord('z') +1 - ord(c) > k:
            ans.append(c)
        else:
            ans.append('a')
            k -= ord('z') + 1 - ord(c)
    if k > 0:
        k = k % 26
        ans[-1] = chr(ord(ans[-1])+k)

    return ''.join(ans)

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=main(s,k)
    printans(ans)
