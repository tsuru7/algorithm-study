def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    x=input()
    return x

def main(x):
    p = x.find('.')
    if p == -1:
        return x
    return x[:p]

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
