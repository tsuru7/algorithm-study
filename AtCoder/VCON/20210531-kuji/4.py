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
    h,w=m_input()
    amap = []
    for _ in range(h):
        amap.append(l_input())
    return h, w, amap

def main(h, w, amap):
    ans = []
    for row in range(h):
        for col in range(w):
            if row == h-1 and col == w-1:
                continue
            if amap[row][col] % 2 == 1:
                amap[row][col] -= 1
                if col == w-1:
                    amap[row+1][col] += 1
                    ans.append((row+1, col+1, row+1+1, col+1))
                else:
                    amap[row][col+1] += 1
                    ans.append((row+1, col+1, row+1, col+1+1))
    return ans

def printans(ans):
    print(len(ans))
    for a in ans:
        print(' '.join(map(str, a)))

if __name__=='__main__':
    h, w, amap=readinput()
    ans=main(h, w, amap)
    printans(ans)
