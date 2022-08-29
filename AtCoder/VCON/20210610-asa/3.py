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
    n,a,b,c,d=m_input()
    s = input()
    return n,a,b,c,d,s

def main(n,a,b,c,d,s):
    s = list(s)
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if c < d:
        if s[d] == '#':
            return 'No'
        for i in range(b+1, d-1):
            if s[i:i+2] == ['#','#']:
                return 'No'
        s[d] = '#'
        if s[c] == '#':
            return 'No'
        for i in range(a+1, c-1):
            if s[i:i+2] == ['#', '#']:
                return 'No'
        return 'Yes'
    elif c == d:
        return 'No'
    else:
        ib = b
        s[ib] = '.'
        while ib <= d and s[ib-1:ib+2] != ['.', '.', '.']:
            ib += 1
        else:
            if s[ib-1:ib+2] != ['.', '.', '.']:
                return 'No'
        s[ib] = '#'
        for ia in range(a+1, c-1):
            if s[ia:ia+2] == ['#', '#']:
                return 'No'
        for i in range(ib+1, d-1):
            if s[i:i+2] == ['#','#']:
                return 'No'
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c,d,s=readinput()
    ans=main(n,a,b,c,d,s)
    printans(ans)
