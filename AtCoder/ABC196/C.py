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
    x = 1
    count = 0
    xx = int(str(x)+str(x))
    while xx <= n:
        count += 1
        x += 1
        xx = int(str(x)+str(x))
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
