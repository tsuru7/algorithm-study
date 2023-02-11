import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    n,k=m_input()
    a=l_input()
    q = i_input()
    lrList = [l_input() for _ in range(q)]
    return n,k,a,q,lrList

def solve(n,k,a,q,lrList):
    m = n // k + 1
    cum = [[0 for _ in range(m)] for _ in range(k)]
    for i in range(k):
        for j in range(m):
            if j == 0:
                cum[i][j] = a[i]
            elif i+j*k < n:
                cum[i][j] = cum[i][j-1] + a[i+j*k]
    # for i in range(k):
    #     cum[i].insert(0,0)
    # print(*cum)

    ans=[]
    for l, r in lrList:
        l -= 1
        r -= 1

        head = r-(k-1)+1
        tail = r
        sub = r-k+1
        # 引く数を計算
        cumi = sub % k
        cumj = sub // k
        # どこから？
        if l-1 >= k:
            subx = cum[cumi][cumj] - cum[cumi][(l-1)//k -1]
        else:
            subx = cum[cumi][cumj]
        print(f'subx: {subx}')
        cumi = head % k
        cumj = head // k
        for _ in range(k-1):
            if l-1 >= k:
                x = cum[cumi][cumj] - cum[cumi][(l-1)//k -1]
            else:
                x = cum[cumi][cumj]
            print(f'x: {x}')
            if x != subx:
                ans.append('No')
                break
            head += 1
            cumi = head % k
            cumj = head // k
        else:
            ans.append('Yes')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,k,a,q,lrList=readinput()
    ans=solve(n,k,a,q,lrList)
    printans(ans)
