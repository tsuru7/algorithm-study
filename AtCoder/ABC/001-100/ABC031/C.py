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
    a=l_input()
    return n,a

def get_points(l, r, a):
    pt = 0
    pa = 0
    for i in range(r-l+1):
        if i % 2 == 0:
            pt += a[l+i]
        else:
            pa += a[l+i]
    return pt, pa

def main(n,a):
    a.insert(0,0)
    points_takahashi = []
    for i in range(1, n+1):
        max_p_aoki = -INFTY
        max_p_takahashi = 0
        for j in range(1, n+1):
            if j == i:
                continue
            l = min(i, j)
            r = max(i, j)
            p_takahashi, p_aoki = get_points(l, r, a)
            if p_aoki > max_p_aoki:
                max_p_aoki = p_aoki
                max_p_takahashi = p_takahashi
                max_j = j
        # print(f'takahashi: {i}, aoki: {max_j}, p_aoki: {max_p_aoki}, p_takahashi: {max_p_takahashi}')
        points_takahashi.append(max_p_takahashi)
    return max(points_takahashi)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
