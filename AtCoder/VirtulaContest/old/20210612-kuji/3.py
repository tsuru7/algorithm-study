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
    n=i_input()
    xylist = []
    for i in range(n):
        xylist.append(l_input()+[i])
    return n,xylist

def main(n,xylist):
    xsorted = sorted(xylist)
    ysorted = sorted(xylist, key=lambda x:x[1])
    candidates = []
    pairs = set()
    candidates.append(abs(xsorted[0][0]-xsorted[-1][0]))
    pairs.add(tuple(sorted((xsorted[0][2], xsorted[-1][2]))))
    candidates.append(abs(xsorted[0][0]-xsorted[-2][0]))
    pairs.add(tuple(sorted((xsorted[0][2], xsorted[-2][2]))))
    candidates.append(abs(xsorted[1][0]-xsorted[-1][0]))
    pairs.add(tuple(sorted((xsorted[1][2], xsorted[-1][2]))))
    pair = tuple(sorted((ysorted[0][2], ysorted[-1][2])))
    if pair not in pairs:
        candidates.append(abs(ysorted[0][1]-ysorted[-1][1]))
    pair = tuple(sorted((ysorted[0][2], ysorted[-2][2])))
    if pair not in pairs:
        candidates.append(abs(ysorted[0][1]-ysorted[-2][1]))
    pair = tuple(sorted((ysorted[1][2], ysorted[-1][2])))
    if pair not in pairs:
        candidates.append(abs(ysorted[1][1]-ysorted[-1][1]))
    candidates.sort(reverse=True)
    ans=candidates[1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist=readinput()
    ans=main(n,xylist)
    printans(ans)
