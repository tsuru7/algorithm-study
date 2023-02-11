def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    p=l_input()
    return n,p

def main(n,p):
    ans=0
    count = 0
    for i in range(n):
        if p[i] == i+1:
            count += 1
        else:
            ans += (count+1)//2
            count = 0
    ans += (count+1)//2
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
