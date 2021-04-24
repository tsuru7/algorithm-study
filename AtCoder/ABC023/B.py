def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    s=input()
    return n,s

def main(n,s):
    t = 'b'
    count = 0
    while len(t) < n:
        count += 1
        if count % 3 == 1:
            t = 'a' + t + 'c'
        elif count % 3 == 2:
            t = 'c' + t + 'a'
        elif count % 3 == 0:
            t = 'b' + t + 'b'
    # print(t)
    if t == s:
        return count
    else:
        return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
