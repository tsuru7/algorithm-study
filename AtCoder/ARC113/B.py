def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b,c=m_input()
    return a,b,c

def main(a,b,c):
    a = a % 10
    if a == 0 or a == 1 or a == 5 or a == 6:
        return a
    elif a == 4 or a == 9:
        if b % 2 == 0:
            return a*a % 10
        else:
            return a
    else:
        b = b % 4
        if b == 0:
            return a*a*a*a % 10
        elif b == 1:
            return a
        else:
            c = c % 4
            return a**(b**c) % 10

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
