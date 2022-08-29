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
    h,w,k=m_input()
    smap = []
    for _ in range(h):
        smap.append(input())
    return h,w,k,smap

def main(h,w,k,smap):
    ans=[[0]*w for _ in range(h)]
    num_st = [0] * h
    for row in range(h):
        num_st[row] = smap[row].count('#')
    
    # print(f'num_st: {num_st}')

    count = 0
    for row in range(h):
        num = num_st[row]
        if num == 0:
            continue
        count += 1
        for col in range(w):
            ans[row][col] = count
            if smap[row][col] == '#' and num > 1:
                count += 1
                num -= 1
    
    for row in range(1, h):
        if num_st[row] == 0:
            for col in range(w):
                if ans[row-1][col] != 0:
                    ans[row][col] = ans[row-1][col]
    
    for row in range(h-1)[::-1]:
        for col in range(w):
            if ans[row][col] == 0:
                ans[row][col] = ans[row+1][col]
            
    return ans

def printans(ans):
    for a in ans:
        print(' '.join(map(str,a)))

if __name__=='__main__':
    h,w,k,smap=readinput()
    ans=main(h,w,k,smap)
    printans(ans)
