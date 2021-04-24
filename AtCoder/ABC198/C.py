from math import sqrt

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    r, x, y = m_input()
    return r, x, y

def main(r, x, y):
    d2 = x**2 + y**2
    if d2 < r**2:
        return 2
    if d2 == r**2:
        return 1
    k = 1
    while (k*r)**2 < d2:
        k += 1
    return k
    
def printans(ans):
    print(ans)

if __name__=='__main__':
    r, x, y=readinput()
    ans=main(r, x, y)
    printans(ans)
