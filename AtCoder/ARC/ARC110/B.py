def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    t=input()
    return n,t

def check_sequence(t):
    n = len(t)
    pattern = '110'
    if t[:3] == '110':
        offset = 0
    elif t[:3] == '101':
        offset = 1
    elif t[:3] == '011':
        offset = 2
    else:
        return False
    for i in range(n):
        if t[i] == pattern[(offset+i)%3]:
            continue
        else:
            return False
    return True

def main(n,t):
    if len(t) == 1:
        if t == '1':
            return 2 * 10**10
        else:
            return 10**10
    if len(t) == 2:
        if t == '11' or t == '10':
            return 10**10
        elif t == '01':
            return 10**10 - 1
        else:
            return 0

    if check_sequence(t) == False:
        return 0

    if t[:3] == '110':
        pattern = 1
    elif t[:3] == '101':
        pattern = 2
    elif t[:3] == '011':
        pattern = 3
    else:
        return 0

    if pattern == 1:
        return ( 3 * 10**10 - n ) // 3 + 1
    elif pattern == 2:
        return ( 3 * 10**10 - n - 1) // 3 + 1
    else:
        return ( 3 * 10**10 - n - 2) // 3 + 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t=readinput()
    ans=main(n,t)
    printans(ans)
