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
    s = input()
    return s

def count_abc(s, i):
    # 最初の'BC'までスキップ。見つからなかったらリターン
    while True:
        if i-1 >= 0 and s[i-1:i+1] == 'BC':
            i -= 2
            break
        elif i == 0:
            return 0, i
        i -= 1
    # 可能な操作回数を数える
    count = 0
    nbc = 1
    while True:
        # print(f'nbc: {nbc}, count: {count}')
        if i >= 0 and s[i] == 'A':
            count += nbc
            i -= 1
        elif i-1 >= 0 and s[i-1:i+1] == 'BC':
            nbc += 1
            i -= 2
        else:
            return count, i

def main(s):
    n = len(s)
    i = n
    ans=0
    while i > 0:
        cnt, i = count_abc(s, i)
        ans += cnt
        # print(i)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
