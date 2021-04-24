def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,k=m_input()
    a=l_input()
    return n,k,a

def main(n,k,a):
    if n == k:
        return 1
    ans = (n-1)//(k-1)
    if (n-1) % (k-1) != 0:
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
