def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s, t = input().split()
    a,b=m_input()
    u = input()
    return s, t, a, b, u

def main(s, t, a, b, u):
    if u == s:
        a -= 1
    else:
        b -= 1
    return (a, b)

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    s, t, a, b, u=readinput()
    ans=main(s, t, a, b, u)
    printans(ans)
