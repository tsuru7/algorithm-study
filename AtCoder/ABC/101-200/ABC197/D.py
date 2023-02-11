from math import pi, cos, sin

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    x0,y0=m_input()
    xh,yh=m_input()
    return n,x0,y0,xh,yh

def main(n,x0,y0,xh,yh):
    xo = (x0+xh)/2
    yo = (y0+yh)/2
    theta = 2.0*pi/n
    xop0 = x0 - xo
    yop0 = y0 - yo
    xop1 = cos(theta)*xop0 - sin(theta)*yop0
    yop1 = sin(theta)*xop0 + cos(theta)*yop0
    x1 = xop1 + xo
    y1 = yop1 + yo
    return (x1, y1)

def printans(ans):
    print(ans[0], ans[1])

if __name__=='__main__':
    n,x0,y0,xh,yh=readinput()
    ans=main(n,x0,y0,xh,yh)
    printans(ans)
