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
    n, r = m_input()
    s = input()
    return n,r,s

def main(n,r,s):
    rightmost = 0
    for i in range(len(s))[::-1]:
        if s[i] == '.':
            rightmost = i
            break
    else:
        return 0
    
    slist = list(s)
    slist.insert(0, '')
    rightmost += 1

    # print(f'rightmost: {rightmost}')

    ans = 0
    i = 1
    while i + r - 1 < rightmost:
        if slist[i] == 'o':
            i += 1
        else:
            for j in range(r):
                slist[i+j] = 'o'
        ans += 1
        # print(f'i: {i}, ans: {ans}, slist: {slist}')
    else:
        for j in range(r):
            slist[i+j] = 'o'
        ans += 1
        # print(f'i: {i}, ans: {ans}, slist: {slist}')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,r,s=readinput()
    ans=main(n,r,s)
    printans(ans)
