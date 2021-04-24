def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b=m_input()
    return a,b

def main(a,b):
    if a+b >= 15 and b >= 8:
        return 1
    elif a+b >= 10 and b>= 3:
        return 2
    elif a+b >= 3:
        return 3
    else:
        return 4

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
