def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,a,b=m_input()
    return n,a,b

def main(n,a,b):
    if a > b:
        return 0
    if n == 1 and a != b:
        return 0
        
    ans=a+(n-1)*b - (b+(n-1)*a-1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    printans(ans)
