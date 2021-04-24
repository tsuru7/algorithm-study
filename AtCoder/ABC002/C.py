def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    x1, y1, x2, y2, x3, y3=m_input()
    return x1, y1, x2, y2, x3, y3

def main(x1, y1, x2, y2, x3, y3):
    a = x2 - x1
    b = y2 - y1
    c = x3 - x1
    d = y3 - y1
    s = 0.5*abs(a*d - b*c)
    return s

def printans(ans):
    print(ans)

if __name__=='__main__':
    x1, y1, x2, y2, x3, y3=readinput()
    ans=main(x1, y1, x2, y2, x3, y3)
    printans(ans)
