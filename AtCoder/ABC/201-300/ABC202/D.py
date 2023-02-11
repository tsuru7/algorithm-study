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
    a,b,k=m_input()
    return a,b,k

memo_count = [ [-1]*31 for _ in range(31)]
def count(na, nb):
    global memo_count
    if memo_count[na][nb] != -1:
        return memo_count[na][nb]
    
    if na == 0 or nb == 0:
        memo_count[na][nb] = 1
        return memo_count[na][nb]

    memo_count[na][nb] = count(na-1, nb) + count(na, nb-1)
    return memo_count[na][nb]
        

memo_ans = ''
def dfs(na, nb, k):
    global memo_ans

    # 'a'で始まる文字列の数
    cnt = count(na-1, nb)
    if k < cnt:
        memo_ans += 'a'
        return dfs(na-1, nb, k)
    elif k == cnt:
        memo_ans += 'a' + 'b'*nb + 'a'*(na-1)
        return memo_ans
    else:
        memo_ans += 'b'
        return dfs(na, nb-1, k-cnt)
        

def main(a,b,k):
    ans = dfs(a, b, k)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=main(a,b,k)
    printans(ans)
