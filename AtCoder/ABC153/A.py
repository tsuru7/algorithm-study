def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    h, a = m_input()
    return h, a

def main(h, a):
    count = h // a
    if h % a != 0:
        count += 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    h, a=readinput()
    ans=main(h, a)
    printans(ans)
