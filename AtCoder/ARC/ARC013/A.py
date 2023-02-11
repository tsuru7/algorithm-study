def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,m,l=m_input()
    p,q,r=m_input()
    return n,m,l,p,q,r

def main(n,m,l,p,q,r):
    ans = 0
    # case1
    ans = max(ans, (l//r)*(m//q)*(n//p))
    ans = max(ans, (l//r)*(m//p)*(n//q))
    ans = max(ans, (l//p)*(m//q)*(n//r))
    ans = max(ans, (l//p)*(m//r)*(n//q))
    ans = max(ans, (l//q)*(m//p)*(n//r))
    ans = max(ans, (l//q)*(m//r)*(n//p))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,l,p,q,r=readinput()
    ans=main(n,m,l,p,q,r)
    printans(ans)
