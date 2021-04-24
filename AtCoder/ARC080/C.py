def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    odd = 0
    four = 0
    for i in range(n):
        if a[i] % 2 != 0:
            odd += 1
        elif a[i] % 4 == 0:
            four += 1
    if odd <= four:
        return 'Yes'
    if (odd == four + 1) and (odd + four == n):
        return 'Yes'
    
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
