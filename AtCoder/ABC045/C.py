import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s = input()
    return s

def main(s):
    l = len(s)
    ans = 0
    for i in range(2**(l-1)):
        sum = 0
        term = s[0]
        formula = s[0]
        b = 1
        for bit in range(l-1):
            # print(f'i: {bin(i)}, b: {bin(b)}')
            if i & b == b:
                sum += int(term)
                term = s[bit+1]
                formula += '+'+s[bit+1]
            else:
                term += s[bit+1]
                formula += s[bit+1]
            b = b << 1
        sum += int(term)
        # print(f'formula: {formula}')
        ans += sum
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
