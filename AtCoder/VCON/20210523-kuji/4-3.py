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
    n,x,m=m_input()
    return n,x,m

def main(n,x,m):
    result = [0]*(m+1)
    a = x
    result[a] = 1
    alist = [a]
    loop = False
    for i in range(2, n+1):
        a = a**2 % m
        if result[a] != 0:
            loop_start = result[a]
            loop_end = i-1
            loop = True
            break
        result[a] = i
        alist.append(a)
    if not loop:
        return sum(alist)
    loop_len = loop_end - loop_start + 1
    loop_count = (n-loop_start+1)//loop_len
    nokori = (n-loop_start+1) % loop_len
    # print(alist)
    # print(result)
    # print(f'loop_start: {loop_start}, loop_end: {loop_end}')
    ans = sum(alist[:loop_start-1]) + sum(alist[loop_start-1:loop_end])*loop_count + sum(alist[loop_start-1:loop_start+nokori-1])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,m=readinput()
    ans=main(n,x,m)
    printans(ans)
