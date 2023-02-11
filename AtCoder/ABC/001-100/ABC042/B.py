def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, l = m_input()
    sList = []
    for _ in range(n):
        sList.append(input())
    return n,l,sList

def main(n,l,sList):
    sList.sort()
    ans=''.join(sList)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l,sList=readinput()
    ans=main(n,l,sList)
    printans(ans)
