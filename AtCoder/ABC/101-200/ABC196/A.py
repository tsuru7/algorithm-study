def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b=m_input()
    c,d=m_input()
    return a,b,c,d

def main(a,b,c,d):
    return b-c

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    printans(ans)
