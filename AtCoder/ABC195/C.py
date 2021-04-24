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
    count = 0
    if n == 10**15:
        count = 5 + 4*(10**15-10**12) + 3*(10**12-10**9) + 2*(10**9 - 10**6) + (10**6 - 10**3)
    elif n >= 10**12:
        count = 4*(n-10**12 +1) + 3*(10**12-10**9) + 2*(10**9 - 10**6) + (10**6 - 10**3)
    elif n >= 10**9:
        count = 3*(n-10**9 +1) + 2*(10**9 - 10**6) + (10**6 - 10**3)
    elif n >= 10**6:
        count = 2*(n - 10**6 +1) + (10**6 - 10**3)
    elif n >= 10**3:
        count = (n - 10**3 +1)
    else:
        count = 0
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
