import sys
sys.setrecursionlimit(10**8)
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

memo = dict()
def func(s, x):
    MOD = 10**9+7
    global memo
    if s+':'+x in memo:
        return memo[s+':'+x]

    # print(f's: {s}, x: {x}')
    temp = 0
    if len(x) == 1:
        count = 0
        for i in range(len(s)):
            if s[i] == x:
                count += 1
        # print(f'count: {count}')
        return count
    
    for i in range(len(s)):
        c = s[i]
        if c == x[0]:
            temp += func(s[i+1:], x[1:])

    temp = temp % MOD
    memo[s+':'+x] = temp
    # print(f'temp: {temp}')
    return temp

def main(s):
    t = ''
    for c in s:
        if c in 'chokudai':
            t += c
    
    ans=func(t, 'chokudai')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
