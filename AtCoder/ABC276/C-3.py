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
    n=i_input()
    p=l_input()
    return n,p

def next_permutation(p):
    '''
    1. 末尾から降順になっている最長の部分列を探す⇒ p_last とする
    2. p_lastの長さがlen(p)ならNoneを返す
    3. 1つ前の要素を p_pre とする
    4. p_lastにp_preを追加する
    5. p_lastを昇順にソートする
    4. p_lastの中からp_preより大きい値の最小値(1.の条件より必ず存在する)を求め、p_lastの先頭へ移動する
    6. pを返す
    '''
    from bisect import bisect_right

    n = len(p)
    p_last_start = 0
    for i in range(n-1)[::-1]:
        if p[i] <= p[i+1]:
            p_last_start = i+1
            break
    if p_last_start == 0:
        return None
    p_last = p[p_last_start-1:]
    p_pre = p[p_last_start-1]
    p_last.sort()
    idx = bisect_right(p_last, p_pre)
    p_last = [p_last[idx]] + p_last[:idx] + p_last[idx+1:]
    return p[:p_last_start-1] + p_last

def prev_permutation(p):
    '''
    1. 末尾から昇順になっている最長の部分列を探す⇒ p_last とする
    2. p_lastの長さがlen(p)ならNoneを返す
    3. 1つ前の要素を p_pre とする
    4. p_lastにp_preを追加する
    5. p_lastを昇順にソートする
    6. p_lastの中からp_preより小さい値の最大値(1.の条件より必ず存在する)を求め、p_lastから取り除く
    7. p_last を反転する
    8. [p_pre] + p_lastを pの残りと結合して返す
    '''
    from bisect import bisect_left

    n = len(p)
    p_last_start = 0
    for i in range(n-1)[::-1]:
        if p[i] >= p[i+1]:
            p_last_start = i+1
            break
    if p_last_start == 0:
        return None
    p_last = p[p_last_start-1:]
    p_pre = p[p_last_start-1]
    p_last.sort()
    idx = bisect_left(p_last, p_pre)
    p_pre_new = p_last[idx-1]
    p_last_rest = (p_last[:idx-1] + p_last[idx:])[::-1]
    p_last = [p_pre_new] + p_last_rest
    return p[:p_last_start-1] + p_last

def solve(n,p):
    return prev_permutation(p)

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
