def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    c = input()
    return c

def main(c):
    return chr(ord(c)+1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    c=readinput()
    ans=main(c)
    printans(ans)
