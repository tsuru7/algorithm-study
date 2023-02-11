def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    return n

def enlongpw(s):
    ans = []
    if len(s) == 0:
        return ['a', 'b', 'c']
        
    for pw in s:
            ans.append(pw+'a')
            ans.append(pw+'b')
            ans.append(pw+'c')
    return ans

def main(n):
    ans = ''
    for _ in range(n):
        ans = enlongpw(ans)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
