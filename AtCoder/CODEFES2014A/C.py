def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b=m_input()
    return a,b

def count_uru(y):
    count = y // 4
    count -= y // 100
    count += y // 400
    return count

def main(a,b):
    return count_uru(b) - count_uru(a-1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
