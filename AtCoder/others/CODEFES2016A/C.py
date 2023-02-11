import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s=input()
    k=i_input()
    return s,k

def main(s,k):
    ans = ''
    for i, c in enumerate(s):
        if i == len(s) -1:
            break
        if c == 'a':
            ans += 'a'
        elif ord('z')+1-ord(c) <= k:
            ans += 'a'
            k -= ord('z')+1-ord(c)
        else:
            ans += c
        # print(ans, k)
    k = k % 26
    if ord('z')+1-ord(s[-1]) > k:
        ans += chr(ord(s[-1])+k)
    else:
        ans += chr(ord(s[-1])+k-26)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=main(s,k)
    printans(ans)
