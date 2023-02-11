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
    n = len(s)
    ans = 0
    for i in range(1, n+1):
        if s[i-1] == 'U':
            ans += n-i
            ans += (i-1)*2
        else:
            ans += (n-i)*2
            ans += i-1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
