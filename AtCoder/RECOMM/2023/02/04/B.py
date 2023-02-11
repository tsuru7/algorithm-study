import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
import string

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
    s1 = input()
    s2 = input()
    s3 = input()
    return s1, s2, s3

def next_char(state):
    s1, s2, s3 = state
    maxlen = max(len(s1), len(s2), len(s3))
    for keta in range(maxlen):
        if len(s1) >= keta+1 and s1[keta] in string.ascii_letters:
            return s1[keta]
        if len(s2) >= keta+1 and s2[keta] in string.ascii_letters:
            return s2[keta]
        if len(s3) >= keta+1 and s3[keta] in string.ascii_letters:
            return s3[keta]
    return None

def judge(state):
    s1, s2, s3 = state
    dlen1 = 0
    for c in s1[::-1]:
        if c not in string.digits:
            break
        dlen1 += 1
    dlen2 = 0
    for c in s2[::-1]:
        if c not in string.digits:
            break
        dlen2 += 1
    dlen3 = 0
    for c in s3[::-1]:
        if c not in string.digits:
            break
        dlen3 += 1
    mindlen = min(dlen1, dlen2, dlen3)
    carry = 0
    for keta in range(mindlen):
        n1 = int(s1[keta])
        n2 = int(s2[keta])
        n3 = int(s3[keta])
        if (n1+n2+carry)%10 != n3:
            return False
        carry = (n1+n2+carry)//10
    return True


def dfs(state, ans):
    '''
    state: 現在の文字列の状態 (s1, s2, s3)
    ans: 現在の答えの状態
    '''
    s1, s2, s3 = state
    # print(f's1: {s1}, s2: {s2}, s3: {s3}, ans: {ans}')
    c = next_char(state) # 次に割り当てる文字を抽出
    # print(f'next_char: {c}')
    if c is None:
        n1 = int(''.join(s1))
        n2 = int(''.join(s2))
        n3 = int(''.join(s3))
        # print(f'n1: {n1}, n2: {n2}, n3: {n3}')
        if n1 == 0 or n2 == 0 or n3 == 0:
            return False
        if n3 == n1 + n2:
            return True
        else:
            return False
    
    # print(f'ans: {ans}')
    for nc in range(10):
        if str(nc) in ans.values():
            continue
        s1 = [str(nc) if cc == c else cc for cc in s1]
        s2 = [str(nc) if cc == c else cc for cc in s2]
        s3 = [str(nc) if cc == c else cc for cc in s3]
        state = [s1, s2, s3]
        if judge(state):
            ans[c] = str(nc)
            result = dfs(state, ans)
            if result:
                return True
            del ans[c]
        s1 = [c if cc == str(nc) else cc for cc in s1]
        s2 = [c if cc == str(nc) else cc for cc in s2]
        s3 = [c if cc == str(nc) else cc for cc in s3]
    state = (s1, s2, s3)
    return False
                    

def solve(s1, s2, s3):
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    state = [s1, s2, s3]
    ans = dict()
    if dfs(state, ans):
        for i in range(len(s1)):
            if s1[i] in ans:
                s1[i] = ans[s1[i]]
        for i in range(len(s2)):
            if s2[i] in ans:
                s2[i] = ans[s2[i]]
        for i in range(len(s3)):
            if s3[i] in ans:
                s3[i] = ans[s3[i]]
        s1 = ''.join(s1)
        s2 = ''.join(s2)
        s3 = ''.join(s3)
        return (s1, s2, s3)
    else:
        return ('UNSOLVABLE')

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    s1, s2, s3=readinput()
    ans=solve(s1, s2, s3)
    printans(ans)
