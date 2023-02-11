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
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    a.insert(0,0)
    b = []
    for i in range(n+1):
        b.append(a[i]-i)
    b = sorted(b[1:])
    lenb = len(b)
    mid = (lenb-1) // 2 
    
    # print(b, mid, b[mid])

    ans = 0
    for i in range(lenb):
        ans += abs(b[i] - b[mid])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
