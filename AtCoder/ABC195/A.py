def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    m,h=m_input()
    return m,h

def main(m,h):
    if h % m == 0:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    m,h=readinput()
    ans=main(m,h)
    printans(ans)
