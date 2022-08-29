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
    n,c=m_input()
    queries = [l_input() for _ in range(n)]
    return n,c,queries

def solve(n,c,queries):
    # Th: Through
    # On: On
    # Of: Off
    # Fl: Flip
    op = ['Th' for _ in range(32)]    
    x = c
    ans=[]
    for t, a in queries:
        bit = ('0'*32+bin(a)[2:])[-32:]
        # print(f'bit: {bit}')
        if t == 1: # AND
            for i in range(32):
                if bit[31-i] == '0':
                    op[i] = 'Of'
                # else:
                #     op[i] = 'Th'
        elif t == 2: # OR
            for i in range(32):
                if bit[31-i] == '1':
                    op[i] = 'On'
                # else:
                #     op[i] = 'Th'
        else: # XOR
            for i in range(32):
                if bit[31-i] == '1':
                    if op[i] == 'On':
                        op[i] = 'Of'
                    elif op[i] == 'Of':
                        op[i] = 'On'
                    elif op[i] == 'Fl':
                        op[i] = 'Th'
                    else:
                        op[i] = 'Fl'
                # else:
                #     op[i] = 'Th'
        # print(f't: {t}, op: {op[::-1]}')
        for i in range(32):
            if op[i] == 'Th':
                continue
            elif op[i] == 'On':
                x |= 1<<i
            elif op[i] == 'Of':
                x &= ~(1<<i)
            elif op[i] == 'Fl':
                x ^= 1<<i
        ans.append(x)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,c,queries=readinput()
    ans=solve(n,c,queries)
    printans(ans)
