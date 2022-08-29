import sys
sys.setrecursionlimit(10**6)
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
    xylist = [ l_input() for _ in range(4) ]
    return xylist

def ccw(p1, p2, p3):
    """3点間の位置関係を判別する

    Parameters
    ----------
    p1, p2, p3: 点の座標(タプルまたはリスト)

    Returns
    -------
     1: 線分12からみて、点3の位置は反時計回り (counter-clockwise)
    -1: 線分12からみて、点3の位置は時計回り (clockwise)
     0: 点3は線分12上にある(線分12の両端を含む) (on-segment)
     2: 点3は線分12の延長線上にあり、点1から見て点2と反対側にある (online-back)
    -2: 点3は線分12の延長線上にあり、点1から見て点2の向こう側にある (online-front)

    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]

    x12 = x2 - x1
    y12 = y2 - y1
    x13 = x3 - x1
    y13 = y3 - y1
    outer = x12*y13 - x13*y12
    if outer > 0:
        return 1 # counter-clockwise
    elif outer < 0:
        return -1 # clockwise
    
    inner = x12*x13 + y12*y13
    if inner < 0:
        return 2 # online-back
    if x12*x12+y12*y12 < x13*x13+y13*y13:
        return -2 # online-front
    return 0 # on-segment

def isSegmentsIntersect(p1, p2, p3, p4):
    """線分12と線分34が交差するかを判別する (端点が重なる場合も交差とみなす)

    Parameters
    ----------
    p1, p2, p3, p4: 線分12、線分34の端点の座標のタプルまたはリスト

    Reterns
    ----------
    True/False: 交差する場合 True、交差しない場合 False

    """
    if ccw(p1, p2, p3)*ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1)*ccw(p3, p4, p2) <= 0:
        return True
    else:
        return False


def solve(xylist):
    p1 = xylist[0]
    p2 = xylist[1]
    p3 = xylist[2]
    p4 = xylist[3]

    if isSegmentsIntersect(p1, p2, p3, p4):
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    xylist=readinput()
    ans=solve(xylist)
    printans(ans)
