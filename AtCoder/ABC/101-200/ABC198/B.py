def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    return n

def main(n):
    if n == 0:
        return 'Yes'
    s = str(n)
    while s[-1] == '0':
        s = s[:-1]
        # print(s)
    for i in range(len(s)//2+1):
        # print(s[i], s[-(i+1)])
        if s[i] == s[-(i+1)]:
            continue
        else:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
