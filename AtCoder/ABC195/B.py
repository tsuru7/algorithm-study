def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b,w=m_input()
    return a,b,w

def main(a,b,w):
    found = False
    for n in range(1, 10**6+1):
        if n*a <= w*1000 and w*1000 <= n*b:
            if not found:
                found = True
                minn = n
            if found:
                maxn = n
    if found:
        return (minn, maxn)
    else:
        return ()

def printans(ans):
    if len(ans) == 2:
        print(ans[0], ans[1])
    else:
        print('UNSATISFIABLE ')

if __name__=='__main__':
    a,b,w=readinput()
    ans=main(a,b,w)
    printans(ans)
